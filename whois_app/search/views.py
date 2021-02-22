import datetime
import subprocess
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import User, Search
from .forms import SearchForm, UserForm
from .mixins import LoginMixin

import whois
# Create your views here.

class HomePageView(LoginMixin, View):
    def get(self, request):
        form = SearchForm
        search = Search.objects.filter(user = request.user.id)
        return render(request, 'home.html', {'form': form, 'search': search})


class PreviousSearchView(LoginMixin, View):
    def post(self, request):
        if request.method == 'POST':
            searchdomain = request.POST['searchdomain']
            domain = whois.whois(searchdomain)
            domain_name = domain.domain_name
            print(domain)
            try:
                creation_date = domain.creation_date[0]
                expiration_date = domain.expiration_date[0]
            except Exception:
                creation_date = domain.creation_date
                expiration_date = domain.expiration_date
            org = domain.org
            date = datetime.datetime.now()
            city = domain.city
            state = domain.state
            zipcode = domain.zipcode
            country = domain.country
            search = Search(
                searchdomain = domain_name,
                org = org,
                city = city,
                state = state,
                zipcode = zipcode,
                country = country,
                user = User.objects.get(id = request.user.id),
                creation_date = creation_date,
                expiration_date = expiration_date,
                date = date
            )
            search.save()
        return redirect('/')

class SignupView(View):
    def get(self, request): 
        form = UserForm
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        if request.method =='POST': 
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user = User(
                username = username,
                email = email,
                first_name = first_name,
                last_name = last_name
            )
            user.set_password(password)
            user.save()
            return redirect('/login')


class DeleteView(LoginMixin, View):
    def get(self, request, pk):
        pk = self.kwargs.get('pk')
        domain = Search.objects.filter(id=pk)
        domain.delete()
        return redirect('/')
