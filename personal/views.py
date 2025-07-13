from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'personal/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'

@login_required
def inicio(request):
    return render(request, 'personal/inicio.html')
