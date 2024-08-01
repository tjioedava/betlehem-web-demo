from django.urls import path
from .views import render_home, render_form

urlpatterns = [
    path('home', render_home, name = 'render_home'),
    path('input', render_form, name = 'render_input')
]