from django.urls import  path
from empleados import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista_empleados, name='lista_empleados'),
    path('detalle/<int:empleado_id>/', views.detalle_empleados, name='detalle_empleados'),  # Patrón de URL corregido
    path('crear/', views.crear_empleado, name='crear_empleado'),
    path('editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
   
    # Otros patrones de URL...
]
