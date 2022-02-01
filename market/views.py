from django.shortcuts import render, redirect, reverse
from django.views import generic 
from .forms import CustomUserCreationForm

# Create your views here.
class LandingPageView(generic.TemplateView):
    template_name = 'market/landing_page.html'

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")