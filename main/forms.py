from django import forms
from .models import *
class Movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields= ('name', 'director', 'cast', 'description', 'date', 'image' )
class Reviewform(forms.ModelForm):
    class Meta:
        model= Review
        fields =("comment", "rating")
