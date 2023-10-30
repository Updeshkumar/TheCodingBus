from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('quiz_view/', views.quiz_view, name='quiz_view'),
    path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
    path('cat/<int:id>/', views.readcat, name="blog_cat"),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    path('calculate_score/', views.calculate_score, name='calculate_score'),  # Ensure this line is present.
]
