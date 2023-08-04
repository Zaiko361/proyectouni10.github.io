from django.urls import path
from inicioApp import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('', views.iniciodef, name='inicio'),
    path('principal/', views.principalDef, name='principal'),
    path('materia/', views.materiaDef, name='materia'),
    path('plan/', views.planDef, name='plan'),
    path('version/', views.versionDef, name='version'),
    path('pdf/<int:informativo_id>/', views.pdfDef, name='pdfDef'),
    path('login/', views.login_view, name='login'),
    path('guardar_informacion/', views.guardar_informacion, name='guardar_informacion'),
    path('guardar_informacion2/', views.guardar_informacion2, name='guardar_informacion2'),
    path('ensenar_informacion/', views.ensenar_informacion, name='ensenar_informacion'),
    path('ensenar_informacion2/', views.ensenar_informacion2, name='ensenar_informacion2'),
    path('ensenar_informacion3/', views.ensenar_informacion3, name='ensenar_informacion3'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('borrar/<int:id_informativo>/', views.borrar_informacion, name='borrar_informativo'),
    path('admin/', admin.site.urls),
]

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Resto de las importaciones

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
