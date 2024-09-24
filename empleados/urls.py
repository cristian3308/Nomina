from django.urls import  path
from . import views

urlpatterns = [
    path('crear/', views.crear_empleado, name='crear_empleado'),
    path('editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    
]
