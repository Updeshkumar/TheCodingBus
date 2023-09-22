from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random

def quiz(request):
    contaxt = {"categories": Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
        
    return render(request, "quiz/home.html", contaxt)

def quiz_show(request):
    return render(request, 'quiz/quiz.html')


def get_quiz(request):
    try:
       question_objs = Question.objects.all()
       if request.GET.get('catgory'):
           question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('catgory'))
       question_objs = list(question_objs)
       print(question_objs)
       
       question_objs = list(question_objs)
       data = []
       random.shuffle(question_objs)
       for question_obj in question_objs:
            print(question_obj)
            data.append({
               "category" : question_obj.category.category_name,
               "question" : question_obj.question,
               "marks": question_obj.marks,
               "answers": question_obj.get_answers()
            }) 
            payload = {'status': True, 'data': data}
            return JsonResponse(payload)
        
    except Exception as e:
        print(e)
    return HttpResponse("Something went Worng")
