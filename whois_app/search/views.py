import datetime
import subprocess
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import User, Search
from .forms import SearchForm, UserForm

import whois
# Create your views here.

class HomePageView(View):
    def get(self, request):
        form = SearchForm
        search = Search.objects.filter(user = request.user.id)
        return render(request, 'home.html', {'form': form, 'search': search})


class PreviousSearchView(View):
    def post(self, request):
        if request.method == 'POST':
            searchdomain = request.POST['searchdomain']
            domain = whois.whois(searchdomain) 
            date = datetime.datetime.now()
            domain_name = domain.domain_name
            creation_date = domain.creation_date
            expiration_date = domain.expiration_date
            org = domain.org
            date = domain.date
            city = domain.city
            state = domain.state
            zipcode = domain.zipcode
            country = domain.country
            search = Search(
                searchdomain = domain_name,
                creation_date = domain.creation_date,
                expiration_date = domain.expiration_date,
                org = domain.org,
                city = domain.city,
                state = domain.state,
                zipcode = domain.zipcode,
                country = domain.country,
                date = date,
                user = User.objects.get(id = request.user.id)
            )
            print(search)
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

    # template_name = "registration/signup.html"
    # form_class = UserForm

    # def get_success_url(self):
    #     return reverse("search:login")