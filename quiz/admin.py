from django.contrib import admin
from .models import Category, Answer, Question

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
