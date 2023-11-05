from django.contrib import admin
# Register your models here.
from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 4  
# in admin page create vote choice 

class QuestionAdmin(admin.ModelAdmin):
	inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
