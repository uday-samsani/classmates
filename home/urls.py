from django.urls import path, include

from . import views as homeViews

urlpatterns = [
    path('', homeViews.index,name='index'),
]