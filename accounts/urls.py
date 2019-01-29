from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views as accountsViews


urlpatterns =[
    path('signin/', accountsViews.signIn, name='signIn'),
    path('', LoginView.as_view(template_name='accounts/login.html'), name='logIn'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logOut'),
    path('edit/', accountsViews.editProfile, name='editProfile'),
]