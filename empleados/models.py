from django.db import models

class Puesto(models.Model):
    nombre_puesto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_puesto

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_contratacion = models.DateField()
    puesto = models.ForeignKey(Puesto, null=True, blank=True, on_delete=models.SET_NULL)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Deduccion(models.Model):
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Bonos(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion

class Nomina(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    salario_bruto = models.DecimalField(max_digits=10, decimal_places=2)
    deducciones = models.DecimalField(max_digits=10, decimal_places=2)
    salario_neto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Nomina {self.fecha_pago} de {self.empleado}'

# Tablas Intermedias para las Relaciones Muchos a Muchos
class NominaDeduccion(models.Model):
    nomina = models.ForeignKey(Nomina, on_delete=models.CASCADE)
    deduccion = models.ForeignKey(Deduccion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nomina', 'deduccion')

class EmpleadoBono(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    bono = models.ForeignKey(Bonos, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('empleado', 'bono')
