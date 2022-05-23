#creating form for user to enter and submit information
from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        field = ['text']
        labels = {'text': ''}
         
