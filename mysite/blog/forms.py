from turtle import width
from django import forms
from django import forms
from .models import Comment

# forms.Form because the form isn't related to a model in models.py
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


# forms.ModelForm used because have to build a form dynamically from the Comment model
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
