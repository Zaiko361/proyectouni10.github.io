from django import forms
from .models import AporteTeorico
from .models import Informativo, AportePerfil, Objetivo_especifico, AmbienteAprendizaje

class InformativoForm(forms.ModelForm):
    class Meta:
        model = Informativo
        fields = '__all__'


class AporteTeoricoForm(forms.ModelForm):
    class Meta:
        model = AporteTeorico
        fields = ['nombre', 'detalle', 'id_asignatura']
        widgets = {
            'detalle': forms.Textarea(attrs={'rows': 4, 'cols': 103}),
        }


class AportePerfilForm(forms.ModelForm):
    class Meta:
        model = AportePerfil
        fields = ['nombre', 'detalle', 'id_asignatura']
        widgets = {
            'detalle': forms.Textarea(attrs={'rows': 4, 'cols': 103}),
        }

class Objetivo_especificoForm(forms.ModelForm):
    class Meta:
        model = Objetivo_especifico
        fields = ['nombre', 'detalle', 'id_asignatura']
        widgets = {
            'detalle': forms.Textarea(attrs={'rows': 4, 'cols': 103}),
        }

class AmbienteAprendizajeForm(forms.ModelForm):
    class Meta:
        model = AmbienteAprendizaje
        fields = ['nombre', 'detalle']
        widgets = {
            'detalle': forms.Textarea(attrs={'rows': 8, 'cols': 103}),
        }

