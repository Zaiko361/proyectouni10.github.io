# Generated by Django 4.2.1 on 2023-07-26 21:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicioApp', '0009_itemunidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aporteteorico',
            name='detalle',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
