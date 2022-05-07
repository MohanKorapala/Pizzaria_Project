from django import forms

from .models import Pizza, Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['text']
        labels = {'text':''} 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''} 
        widgets = {'text': forms.Textarea(attrs={'cols':80})} 