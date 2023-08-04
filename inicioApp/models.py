from django.db import models
from django.contrib.auth.models import User

class asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Syllabus(models.Model):
    id_ver_syllabus = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    version = models.CharField(max_length=10)
    id_usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class Informativo(models.Model):
    id_informativo = models.AutoField(primary_key=True)
    carrera = models.CharField(max_length=60)
    informacion = models.CharField(max_length=200)
    id_asignatura = models.ForeignKey(asignatura, null=True, on_delete=models.SET_NULL)
    periodo = models.CharField(max_length=20)
    prerrequisito = models.CharField(max_length=50, blank=True)
    correquisito = models.CharField(max_length=50, blank=True)
    profesional = models.CharField(max_length=50, blank=True)
    unidad_organ = models.CharField(max_length=20)
    horas_docencia = models.IntegerField()
    horas_prac_docente = models.IntegerField()
    horas_pract_autonoma = models.IntegerField()
    horas_trab_autonomo = models.IntegerField()
    objetivo_general = models.CharField(max_length=400, blank=True)
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)
    id_usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.informacion

class Objetivo_especifico(models.Model):
    id_objetivo_especifico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    detalle = models.CharField(max_length=500)
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)
    id_asignatura = models.ForeignKey(asignatura, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class AporteTeorico(models.Model):
    id_aporte_teorico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    detalle = models.CharField(max_length=500)
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)
    id_asignatura = models.ForeignKey(asignatura, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class AportePerfil(models.Model):
    id_aporte_perfil = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    detalle = models.CharField(max_length=500)
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)
    id_asignatura = models.ForeignKey(asignatura, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class AmbienteAprendizaje(models.Model):
    id_ambiente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    detalle = models.CharField(max_length=2000)
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.detalle


class Responsable(models.Model):
    responsable_id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    firma = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)
    id_asignatura = models.ForeignKey(asignatura, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    id_unidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    detalle = models.CharField(max_length=500)
    objetivo = models.CharField(max_length=500)
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre


class ItemUnidad(models.Model):
    id_item = models.AutoField(primary_key=True)
    contenido = models.CharField(max_length=100)
    hora_docencia = models.IntegerField()
    hora_practica = models.IntegerField()
    horas_autonomas = models.IntegerField()
    id_unidad = models.ForeignKey(Unidad, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.contenido


class Referencia(models.Model):
    referencia_id = models.AutoField(primary_key=True)
    basica = models.CharField(max_length=100)
    complementaria = models.CharField(max_length=100, blank=True)
    sitioweb = models.CharField(max_length=100, blank=True)
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.basica


class ProductoAcademico(models.Model):
    id_prod_academico = models.AutoField(primary_key=True)
    objetivo = models.CharField(max_length=1000)
    productos_parciales = models.CharField(max_length=1000, blank=True)
    resultados = models.CharField(max_length=1000, blank=True)
    integracion = models.CharField(max_length=1000, blank=True)
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.objetivo

class ProductoAcademicoItem(models.Model):
    id_prod_academicoItem = models.AutoField(primary_key=True)
    detalle = models.CharField(max_length=1000)
    id_ver_syllabus = models.ForeignKey(Syllabus, null=True, on_delete=models.SET_NULL)

class Docente(models.Model):
    id_Profesores = models.AutoField(primary_key=True)
    docente_nombre = models.CharField(max_length=1000)
    firma = models.CharField(max_length=1000)
    fecha_creacion = models.DateField()
    id_asignatura = models.ForeignKey(asignatura, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.docente_nombre


class Docente2(models.Model):
    id_Profesores2 = models.AutoField(primary_key=True)
    nombreJefe = models.CharField(max_length=100)
    nombreCoordinador = models.CharField(max_length=100)
    id_asignatura = models.ForeignKey(asignatura, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombreCoordinador


