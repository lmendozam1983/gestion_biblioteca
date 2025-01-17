from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, LibroForm, PrestamoForm, SignInForm
from django.contrib import messages
from .models import Libro, Prestamo
from .forms import UserForm 
from django.http import HttpResponseRedirect

# Create your views here.

def mostrar_usuario(request):
    usuarios = User.objects.all()
    return render(request, 'mostrar_usuario.html', {'usuarios': usuarios})

def editar_usuario(request, id_usuario):
    return render(request, 'editar_usuario.html', {'id_usuario': id_usuario})

def eliminar_usuario(request, id_usuario):
    return render(request, 'eliminar_usuario.html', {'id_usuario': id_usuario})

def test_view(request):
    return render(request, 'test.html')

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Loguear al usuario
                login(request, user)  # Aquí pasamos correctamente `request` y `user`
                return redirect('/')  # Redirige a la página principal o a donde prefieras
            else:
                form.add_error(None, "Usuario o contraseña incorrectos")
    else:
        form = SignInForm()

    return render(request, 'signin.html', {'form': form})

from django.contrib.auth import authenticate, login

def nuevo_usuario(request):
    if request.method == "POST":
        form = UserForm(request.POST)  # Ajusta el nombre del formulario si es diferente
        if form.is_valid():
            # Guardar el nuevo usuario
            user = form.save()
            # Autenticar y loguear al usuario automáticamente
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Asegúrate de que este es el campo correcto
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Inicia sesión
                messages.success(request, "Usuario creado exitosamente. Has iniciado sesión.")
                return redirect('/')  # Redirige a la página principal o a donde prefieras
            else:
                messages.error(request, "No se pudo autenticar al usuario automáticamente.")
        else:
            messages.error(request, "Error al crear el usuario. Revisa los datos proporcionados.")

    # Si es un GET o cualquier otro método, muestra un formulario vacío
    form = UserForm()
    return render(request, 'nuevo_usuario.html', {'form': form})


def logoutView(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')

def libros_view(request):
    libros = Libro.objects.all()
    return render(request, 'mostrar_libros.html', {'libros': libros})

def ingresar_libro_view(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            return redirect('mostrar_libros')
    else:
        form = LibroForm()
    return render(request, 'ingresar_libros.html', {'form': form})

def editar_libro_view(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('mostrar_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'editar_libros.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect, render
from .models import Libro

def eliminar_libro_view(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('mostrar_libros')  # Redirige después de eliminar el libro

    return render(request, 'eliminar_libros.html', {'libro': libro})

def detalle_libros_view(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'detalle_libros.html', {'libro': libro})

def lista_prestamo_libro_view(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'lista_prestamo_libros.html', {'prestamos': prestamos})

def nuevo_prestamo_libro_view(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save()
            return redirect('lista_prestamo')
    else:
        form = PrestamoForm()
    return render(request, 'prestamo_libros.html', {'form': form})

def editar_prestamo_libro_view(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamo')
    else:
        form = PrestamoForm(instance=prestamo)

    return render(request, 'editar_prestamo.html', {'form': form})

def eliminar_prestamo_libro_view(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('lista_prestamo')  # Redirige después de eliminar el prestamo

    return render(request, 'eliminar_prestamo.html', {'prestamo': prestamo})






