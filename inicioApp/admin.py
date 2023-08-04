from django.contrib import admin
from .models import *

admin.site.register(asignatura)
admin.site.register(Informativo)
admin.site.register(Responsable)
admin.site.register(Unidad)
admin.site.register(ItemUnidad)
admin.site.register(AmbienteAprendizaje)
admin.site.register(Referencia)
admin.site.register(ProductoAcademico)
admin.site.register(Syllabus)
admin.site.register(ProductoAcademicoItem)
admin.site.register(Docente)
admin.site.register(Docente2)

from django.contrib import admin
from .forms import AporteTeoricoForm, AportePerfilForm, AmbienteAprendizajeForm

@admin.register(AporteTeorico)
class AporteTeoricoAdmin(admin.ModelAdmin):
    form = AporteTeoricoForm

@admin.register(AportePerfil)
class AportePerfilAdmin(admin.ModelAdmin):
    form = AportePerfilForm



@admin.register(Objetivo_especifico)
class AmbienteAprendizajeAdmin(admin.ModelAdmin):
    form = AmbienteAprendizajeForm
