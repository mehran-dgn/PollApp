from django.contrib import admin
from .models import Question  , Choice 
# Register your models here.


#There is also StackedInline
class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra = 3 

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date" , "question_text"]

    list_display = ["pub_date","question_text" , "was_published_recently"]

    list_filter = ["pub_date"]

    search_fields = ["question_text"]

    fieldsets = [
        (None , {"fields":["question_text"]}) , 
        ("Date information" , {"fields":["pub_date"]}),
    ]
    inlines = [ChoiceInline]



admin.site.register(Question , QuestionAdmin)
admin.site.register(Choice)