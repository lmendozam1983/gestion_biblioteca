from django.urls import path
from . import views

urlpatterns = [
    path('mostrar_usuario/', views.mostrar_usuario, name='mostrar_usuario'),
    path('nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logoutView, name='logout'),
    path('test/', views.test_view, name='test'),
    path('mostrar_libros/', views.libros_view, name='mostrar_libros'), 
    path('detalle_libros/<int:pk>', views.detalle_libros_view, name='detalle_libros'),
    path('ingresar_libros/', views.ingresar_libro_view, name='ingresar_libros'),
    path('editar_libros/<int:pk>', views.editar_libro_view, name='editar_libros'),
    path('eliminar_libros/<int:pk>', views.eliminar_libro_view, name='eliminar_libros'),
    path('lista_prestamo_libros/', views.lista_prestamo_libro_view, name='lista_prestamo'),
    path('prestamo_libros/',views.nuevo_prestamo_libro_view,name='prestamo_libros'),
    path('editar_prestamo/<int:pk>', views.editar_prestamo_libro_view,name='editar_prestamo'),
    path('eliminar_prestamo/<int:pk>', views.eliminar_prestamo_libro_view,name='eliminar_prestamo'),
]