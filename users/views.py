from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import *

from .forms import CustomUserCreationForm


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

