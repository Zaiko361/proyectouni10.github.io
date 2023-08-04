# Generated by Django 4.2.1 on 2023-07-27 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicioApp', '0012_asignatura_remove_informativo_asignatura_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aporteperfil',
            name='id_asignatura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.asignatura'),
        ),
        migrations.AddField(
            model_name='aporteteorico',
            name='id_asignatura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.asignatura'),
        ),
        migrations.AddField(
            model_name='responsable',
            name='id_asignatura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.asignatura'),
        ),
    ]