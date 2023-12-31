# Generated by Django 4.2.1 on 2023-07-24 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicioApp', '0008_delete_itemunidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemUnidad',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.CharField(max_length=50)),
                ('hora_docencia', models.IntegerField()),
                ('hora_practica', models.IntegerField()),
                ('gestion_practica', models.IntegerField()),
                ('horas_autonomas', models.IntegerField()),
                ('id_unidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.unidad')),
            ],
        ),
    ]
