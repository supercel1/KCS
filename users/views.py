from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
