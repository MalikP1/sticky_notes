from django import forms
from .models import Posts

'''
Form for creating and updating Post objects.
Meta class defines the model to use (Post),
and the fields to include in the form.
'''


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'author']
