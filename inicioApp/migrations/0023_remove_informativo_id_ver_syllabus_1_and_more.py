# Generated by Django 4.2.1 on 2023-08-02 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicioApp', '0022_informativo_id_ver_syllabus_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informativo',
            name='id_ver_syllabus_1',
        ),
        migrations.RemoveField(
            model_name='informativo',
            name='id_ver_syllabus_2',
        ),
        migrations.RemoveField(
            model_name='informativo',
            name='id_ver_syllabus_3',
        ),
    ]
