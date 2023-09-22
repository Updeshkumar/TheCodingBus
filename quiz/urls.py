from django.urls import path
from . import views

app_name = "quiz"
urlpatterns = [
    path('quiz/', views.quiz, name="quiz"),
    path('quiz/get-quiz/', views.get_quiz, name="get_quiz"),
    path('quiz_show/', views.quiz_show, name="quiz_show")
]
