from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

class UserRegisterView(generic.edit.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
