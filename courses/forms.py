from django import forms
from .models import Courses, Memo

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses 
        fields = ['title', 'times']  
        labels = {'title': '講義名', 'times': '回数'}

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo  
        fields = ['memo']  
        labels = {'memo':''}

