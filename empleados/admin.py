from django.contrib import admin
from .models import Puesto, Empleado, Deduccion, Bonos, Nomina, NominaDeduccion, EmpleadoBono

admin.site.register(Puesto)
admin.site.register(Empleado)
admin.site.register(Deduccion)
admin.site.register(Bonos)
admin.site.register(Nomina)
admin.site.register(NominaDeduccion)
admin.site.register(EmpleadoBono)
