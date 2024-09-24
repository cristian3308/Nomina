from django.shortcuts import render, get_object_or_404, redirect
from .models import Empleado 
from .forms import EmpleadoForm # Importa tu modelo de Empleado

def home(request):
    return render(request, 'empleados_nomina/home.html')

def lista_empleados(request):
    empleados = Empleado.objects.all()  # Obtén todos los empleados
    return render(request, 'empleados_nomina/lista_empleados.html', {'empleados': empleados})  # Renderiza un template

def detalle_empleados(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)  # Obtén el empleado por ID o muestra un error 404
    return render(request, 'empleados_nomina/detalle_empleados.html', {'empleado': empleado})  # Renderiza un template

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')  # Redirige a la lista de empleados después de guardar
    else:
        form = EmpleadoForm()
    return render(request, 'empleados_nomina/crear_empleado.html', {'form': form})

def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)  # Obtén el empleado por ID
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)  # Crea el formulario con los datos del empleado
        if form.is_valid():
            form.save()  # Guarda los cambios en la base de datos
            return redirect('lista_empleados')  # Redirige a la lista de empleados después de guardar
    else:
        form = EmpleadoForm(instance=empleado)  # Crea el formulario con los datos del empleado
    return render(request, 'empleados_nomina/editar_empleado.html', {'form': form})