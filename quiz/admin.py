# quizapp/admin.py

from django.contrib import admin
from .models import UserResponse, Question, Choice, Category, UserProfile

admin.site.register(UserProfile)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    

    
    def __str__(self):
        self.name
admin.site.register(Category, CategoryAdmin)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text','category']
    search_fields = ('text',)
    
    

    
    def __str__(self):
        return self.text, self.category
admin.site.register(Question, QuestionAdmin)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['question','selected_choice']
    
    def __str__(self):
        return self.question, self.selected_choice
admin.site.register(UserResponse)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question','text','is_correct']
    search_fields = ('text',)
    def __str__(self):
        return self.is_correct
    
admin.site.register(Choice, ChoiceAdmin)

