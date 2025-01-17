from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Libro, Prestamo
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        
        def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Este correo electrónico ya está en uso.")
            return email
        

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Contraseña")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Nombre de usuario o contraseña incorrectos.")
        return cleaned_data


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        
class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'