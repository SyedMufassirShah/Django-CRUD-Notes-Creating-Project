from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class SignupView(CreateView):
    template_name = 'home/register.html'
    form_class = UserCreationForm
    success_url = '/smart/notes/'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class GreetView(TemplateView):
    template_name = "home/greeting.html"
    extra_context = {"dated": datetime.today()}
    
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'