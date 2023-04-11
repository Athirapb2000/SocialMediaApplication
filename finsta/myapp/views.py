from django.shortcuts import render

from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy

from myapp.forms import SignUpForm

class SignUpView(CreateView):
    model=User
    form_class=SignUpForm
    template_name="register.html"
    success_url=reverse_lazy("register")

    def form_valid(self, form):
        messages.success(self.request,"account has been created!!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
