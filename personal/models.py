from django.db import models
from django.contrib.auth.models import User

# 1. Sede
class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre

# 2. Cargo
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# 3. Empleado
class Empleado(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_ingreso = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=20, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Licencia', 'Licencia')], default='Activo')
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# 4. Tipo de Licencia
class TipoLicencia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# 5. Licencia
class Licencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoLicencia, on_delete=models.PROTECT)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(blank=True)
    aprobado = models.BooleanField(default=False)
    documento_pdf = models.FileField(upload_to='documentos/licencias/', blank=True, null=True)

# 6. Tipo de Baja
class TipoBaja(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# 7. BajaEmpleado
class BajaEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoBaja, on_delete=models.PROTECT)
    fecha_baja = models.DateField()
    motivo = models.TextField()
    observaciones = models.TextField(blank=True)
    documento_pdf = models.FileField(upload_to='documentos/bajas/', blank=True, null=True)

# 8. Asistencia
class Asistencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[('Presente', 'Presente'), ('Tarde', 'Tarde'), ('Ausente', 'Ausente')], default='Presente')

# 9. Falta
class Falta(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.TextField()
    tipo = models.CharField(max_length=20, choices=[('Justificada', 'Justificada'), ('Injustificada', 'Injustificada')], default='Injustificada')

# 10. Vacacion
class Vacacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    aprobado = models.BooleanField(default=False)
    documento_pdf = models.FileField(upload_to='documentos/vacaciones/', blank=True, null=True)

# 11. Horas Extra
class HoraExtra(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    horas = models.DecimalField(max_digits=4, decimal_places=2)

# 12. Día Feriado
class DiaFeriado(models.Model):
    fecha = models.DateField(unique=True)
    descripcion = models.CharField(max_length=255)

# 13. CTS / Gratificación
class PagoExtra(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=[('CTS', 'CTS'), ('Gratificación', 'Gratificación')])
    periodo = models.CharField(max_length=10)  # Ej: "2025-07"
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_calculo = models.DateField()
    documento_pdf = models.FileField(upload_to='documentos/pagos_extras/', blank=True, null=True)

# 14. Turno
class Turno(models.Model):
    nombre = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return self.nombre

# 15. Horario Asignado
class HorarioAsignado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)

# 16. Contrato
class Contrato(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    archivo_pdf = models.FileField(upload_to='documentos/contratos/', blank=True, null=True)

# 17. Capacitacion
class Capacitacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    institucion = models.CharField(max_length=100)
    fecha = models.DateField()
    duracion_horas = models.IntegerField()
    certificado_pdf = models.FileField(upload_to='documentos/capacitaciones/', blank=True, null=True)

# 18. Evaluacion de Desempeño
class EvaluacionDesempeno(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    evaluador = models.CharField(max_length=100)
    fecha = models.DateField()
    puntaje = models.DecimalField(max_digits=4, decimal_places=2)
    comentarios = models.TextField(blank=True)

# 19. Permiso especial
class Permiso(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    motivo = models.TextField()
    aprobado = models.BooleanField(default=False)
    documento_pdf = models.FileField(upload_to='documentos/permisos/', blank=True, null=True)

# 20. Incidente o sanción
class Incidente(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    documento_pdf = models.FileField(upload_to='documentos/incidentes/', blank=True, null=True)

# 21. Log del sistema
class LogSistema(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    modelo_afectado = models.CharField(max_length=100)
    id_objeto = models.IntegerField(null=True, blank=True)
    