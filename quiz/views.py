
from django.shortcuts import render, redirect
from .models import Question, Choice, UserResponse, Category
from django.contrib.sessions.models import Session
import random
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa




app_name = 'quiz'

def quiz_view(request):
    # Clear the session data to reset the quiz
    request.session.clear()
    
    cat = Category.objects.all()
    context = {'cat': cat}
    return render(request, 'quiz/category_list.html', context)


def submit_quiz(request):
    if request.method == 'POST':
        # Initialize or retrieve the user's responses from the session
        user_responses = request.session.get('user_responses', [])
        
        for question_id, choice_id in request.POST.items():
            if question_id.startswith('question_'):
                question_id = int(question_id.split('_')[1])
                choice_id = int(choice_id)
                question = Question.objects.get(id=question_id)
                selected_choice = Choice.objects.get(id=choice_id)

                # Debugging: Print the selected choice and its correctness.
                print(f"Selected Choice: {selected_choice.text}, Is Correct: {selected_choice.is_correct}")

                # Check if the selected choice is correct before creating a UserResponse object
                if selected_choice.is_correct:
                    user_responses.append(question_id)  # Store the question ID
        
        # Store the updated user responses in the session
        request.session['user_responses'] = user_responses

        # After processing the form submission, return a redirect to another view or URL.
        return redirect('quiz:calculate_score')



def calculate_score(request):
    # Retrieve the user's responses from the session
    user_responses = request.session.get('user_responses', [])

    # Calculate the total number of questions attempted
    total_questions = len(user_responses)

    # Check if there are any correct responses
    correct_responses = Question.objects.filter(id__in=user_responses, choice__is_correct=True)
    correct_score = len(correct_responses)

    # Calculate the score based on the presence of correct responses
    if total_questions > 0 and correct_score == 0:
        # If there are questions attempted but no correct responses, set the score to 0
        score = 0
    else:
        # Otherwise, calculate the score based on the number of correct responses
        score = correct_score

    # Store the score in the session
    request.session['score'] = score

    context = {'score': score}
    return render(request, 'quiz/quiz_list.html', context)



def readcat(request, id):
    cats = Category.objects.get(cat_id=id)
    
    # Check if we have already selected questions in this session
    if 'selected_questions' not in request.session:
        all_questions = Question.objects.filter(category=cats)
        
        # Shuffle the questions to randomize their order
        all_questions = list(all_questions)
        random.shuffle(all_questions)

        # Select the first 10 questions (or less if there are fewer than 10)
        selected_questions = all_questions[:10]
        
        # Store the selected questions in the session
        request.session['selected_questions'] = [question.id for question in selected_questions]
    else:
        # Retrieve the selected question IDs from the session and fetch the questions
        selected_question_ids = request.session['selected_questions']
        selected_questions = Question.objects.filter(id__in=selected_question_ids)

    context = {'cat': cats, 'questions': selected_questions}
    return render(request, 'quiz/all_question.html', context)




from django.shortcuts import render, redirect
from .models import Question, Choice, UserResponse, Category, UserProfile
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import UserProfileForm

app_name = 'quiz'

# ... your other views ...

def generate_certificate(request):
    # Retrieve the user's score from the session
    score = request.session.get('score', 0)

    if score == 10:
        # Get user information from the form
        if request.method == 'POST':
            form = UserProfileForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                number = form.cleaned_data['number']
                email = form.cleaned_data['email']
                location = form.cleaned_data['location']

                # Check if a certificate already exists for the user
                existing_certificate = UserProfile.objects.filter(email=email).first()
                
                if existing_certificate:
                    # If a certificate exists, prevent generating another one
                    return render(request, 'quiz/allreadygncer.html')
                else:
                    # Create a new UserProfile or update it if it exists
                    user_profile, created = UserProfile.objects.get_or_create(name=name, number=number, email=email, location=location)

                    # Assign the user's score to the user profile
                    user_profile.score = score
                    user_profile.save()

                    # Load the certificate template
                    template = get_template('quiz/certificate.html')

                    # Define the context for the template, including user information
                    context = {
                        'score': score,
                        'name': name,
                        'number': number,
                        'email': email,
                        'location': location,
                    }

                    # Render the template with the context
                    html = template.render(context)
                    response = HttpResponse(content_type='application/pdf')

                    # Generate the PDF certificate
                    pisa_status = pisa.CreatePDF(html, dest=response)

                    # Check if PDF generation was successful
                    if pisa_status.err:
                        return HttpResponse('Error generating the certificate', status=500)

                    # Set the response headers for downloading the PDF
                    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
                    return response
        else:
            form = UserProfileForm()  # Create an empty form

        context = {
            'form': form,
            'score': score,
            'success_message': 'Your certificate has been generated successfully!',
        }

        return render(request, 'quiz/certificate.html', context)
    else:
        # Display a message when the score is not 10
        return HttpResponse('You did not score a perfect 10, so you are not eligible for a certificate.')
