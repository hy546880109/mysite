from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuetsionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [(None, {'fields':['question_text']}),
                 ('date',{'fields':['pub_date'], 'classes':['collapse']}),
                 ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
admin.site.register(Question,QuetsionAdmin)


