
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('post:index')#После успешной регистрации напрвляем пользователя на главный экран
    template_name = 'users/signup.html'
# Create your views here.
