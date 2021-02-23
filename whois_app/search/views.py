import datetime
import subprocess
import requests
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
            searchdomain = request.POST['searchdomain'] # domain name
            
            # # Parsing it through whois Package

            # domain = whois.whois(searchdomain)

            # Api Response
            response = requests.get('https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_COT8DMZsnQWZUYRQ0K9DWwazlMY7G&domainName=' + searchdomain + '&outputFormat=JSON').json()

            availability = requests.get('https://domain-availability.whoisxmlapi.com/api/v1?apiKey=at_COT8DMZsnQWZUYRQ0K9DWwazlMY7G&domainName=' + searchdomain + '&credits=DA').json()


            availabe = availability['DomainInfo']['domainAvailability']
            if availabe == "AVAILABLE":
                domain_name = response['WhoisRecord']['domainName']
                creation_date = datetime.datetime.now()
                expiration_date = datetime.datetime.now()
                org = 'Not Created'
                date = datetime.datetime.now()
                city = 'Not Created'
                state = 'Not Created'
                country = 'Not Created'
                search = Search(
                    searchdomain = domain_name,
                    org = org,
                    city = city,
                    state = state,
                    country = country,
                    availability = availabe,
                    user = User.objects.get(id = request.user.id),
                    creation_date = creation_date,
                    expiration_date = expiration_date,
                    date = date
                )
                search.save()
            else:
                domain_name = response['WhoisRecord']['domainName']
                creation_date = response['WhoisRecord']['registryData']['createdDate']
                expiration_date = response['WhoisRecord']['registryData']['expiresDate']
                org = response['WhoisRecord']['registrant']['organization']
                date = datetime.datetime.now()
                city = response['WhoisRecord']['registrant']['city']
                state = response['WhoisRecord']['registrant']['state']
                country = response['WhoisRecord']['registrant']['country']
                search = Search(
                    searchdomain = domain_name,
                    org = org,
                    city = city,
                    state = state,
                    country = country,
                    availability = availabe,
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

class ProfileView(LoginMixin, View):
    def get(self, request):
        user = User.objects.filter(id=request.user.id).values()
        search = Search.objects.filter(user = request.user.id).values()
        print(user)
        print(search)
        context = {
            'users': user,
            'search': search
        }
        return render(request, 'profile.html', context)