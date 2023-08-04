# Generated by Django 4.2.1 on 2023-08-02 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicioApp', '0021_docente2_docente'),
    ]

    operations = [
        migrations.AddField(
            model_name='informativo',
            name='id_ver_syllabus_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='informativo_1', to='inicioApp.syllabus'),
        ),
        migrations.AddField(
            model_name='informativo',
            name='id_ver_syllabus_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='informativo_2', to='inicioApp.syllabus'),
        ),
        migrations.AddField(
            model_name='informativo',
            name='id_ver_syllabus_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='informativo_3', to='inicioApp.syllabus'),
        ),
    ]