from django.urls import path, include
from .views import PreviousSearchView, HomePageView

app_name = 'search'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', PreviousSearchView.as_view(), name='search')
]
