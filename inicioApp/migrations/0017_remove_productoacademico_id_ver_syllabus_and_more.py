# Generated by Django 4.2.1 on 2023-07-31 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicioApp', '0016_rename_titulo_obra_referencia_basica_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoacademico',
            name='id_ver_syllabus',
        ),
        migrations.DeleteModel(
            name='ItemProducto',
        ),
        migrations.DeleteModel(
            name='ProductoAcademico',
        ),
    ]
