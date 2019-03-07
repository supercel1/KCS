<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignupView(CreateView):
    form_class = UseCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
>>>>>>> origin/master
