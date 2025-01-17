from django.contrib import admin
from .models import User, Libro, Prestamo
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm

# Register your models here.

class CustomUserCreationForm(UserAdmin):
    add_form = CustomUserCreationForm
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "first_name", "last_name", "password1", "password2"),
        }),
    )
    
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    
admin.site.unregister(User)
admin.site.register(User, CustomUserCreationForm)
    
    
    
    
    
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'disponible')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('titulo', 'disponible')
    ordering = ('titulo', 'id')
    
@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'libro', 'fecha_prestamo', 'fecha_devolucion', 'estado')
    search_fields = ('usuario', 'libro', 'estado')
    list_filter = ('usuario', 'libro')
    ordering = ('usuario', 'libro')
    