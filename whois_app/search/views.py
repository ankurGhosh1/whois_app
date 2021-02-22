import datetime
import subprocess
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import User, Search
from .forms import SearchForm

import whois
# Create your views here.

class HomePageView(View):
    def get(self, request):
        form = SearchForm
        search = Search.objects.all()
        return render(request, 'home.html', {'form': form, 'search': search})

    # template_name = 'home.html'
    # context_object_name = 'search'
    # form_class = SearchForm

    # def get_queryset(self):
    #     search = Search.objects.all()
    #     return search

class PreviousSearchView(View):
    def post(self, request):
        if request.method == 'POST':
            searchdomain = request.POST['searchdomain']
            domain = whois.whois(searchdomain) # subprocess.check_output(['whois', searchdomain]) # whois.query(searchdomain)
            date = datetime.datetime.now()
            print(domain)
            search = Search(
                searchdomain = searchdomain,
                date = date,
                user = User.objects.get(id = request.user.id)
            )
            search.save()
            return redirect('/')
    # template_name = 'search.html'
    # context_object_name = 'search'

    # def get_queryset(self):
    #     search = Search.objects.all()
    #     return queryset
