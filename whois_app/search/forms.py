from django import forms
from .models import User, Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'
        exclude = ('date', 'user')