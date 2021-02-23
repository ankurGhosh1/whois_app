from django.urls import path, include
from .views import PreviousSearchView, HomePageView, SignupView, DeleteView, ProfileView
from django.contrib.auth.views import LoginView, LogoutView 


app_name = 'search'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', PreviousSearchView.as_view(), name='search'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('profile/', ProfileView.as_view(), name='delete')
]
