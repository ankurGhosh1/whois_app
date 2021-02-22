from django import forms
from .models import User, Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'
        exclude = ('date', 'user', 'city', 'state', 'country', 'zipcode', 'expiration_date', 'creation_date', 'org')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('is_superuser', 'is_active', 'is_staff', 'user_permissions', 'date_joined', 'groups', 'last_login')