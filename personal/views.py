from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        user = authenticate(request, username=usuario, password=contrasena)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'login.html')  # Asegúrate de que esté en personal/templates/personal/login.html


@login_required
def inicio(request):
    return render(request, 'inicio.html')  # Crea este archivo HTML también

def logout_view(request):
    logout(request)
    return redirect('login')

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # o a otra página que desees
    else:
        form = UserCreationForm()
    return render(request, 'registrousuario.html', {'form': form})

