# Generated by Django 4.2.1 on 2023-07-21 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicioApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id_asignatura', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id_carrera', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id_ver_syllabus', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
                ('version', models.CharField(max_length=10)),
                ('id_usurio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id_unidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('detalle', models.CharField(max_length=500)),
                ('objetivo', models.CharField(max_length=500)),
                ('id_ver_syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.syllabus')),
            ],
        ),
        migrations.CreateModel(
            name='TipoReferencia',
            fields=[
                ('id_tipo_referencia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('id_ver_syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.syllabus')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('responsable_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('firma', models.CharField(max_length=100)),
                ('fecha_entrega', models.DateField()),
                ('id_ver_syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.syllabus')),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('referencia_id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_obra', models.CharField(max_length=100)),
                ('existencia', models.CharField(blank=True, max_length=50)),
                ('cantidad', models.IntegerField()),
                ('id_tipo_referencia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.tiporeferencia')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoAcademico',
            fields=[
                ('id_prod_academico', models.AutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=500)),
                ('id_ver_syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.syllabus')),
            ],
        ),
        migrations.CreateModel(
            name='ItemUnidad',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.CharField(max_length=50)),
                ('hora_docencia', models.IntegerField()),
                ('hora_practica', models.IntegerField()),
                ('id_unidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='ItemProducto',
            fields=[
                ('itemprod_id', models.AutoField(primary_key=True, serialize=False)),
                ('objetivo', models.CharField(max_length=500)),
                ('productos_parciales', models.CharField(blank=True, max_length=500)),
                ('resultados', models.CharField(blank=True, max_length=500)),
                ('integracion', models.CharField(blank=True, max_length=500)),
                ('id_prod_academico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.productoacademico')),
            ],
        ),
        migrations.CreateModel(
            name='Informativo',
            fields=[
                ('id_informativo', models.AutoField(primary_key=True, serialize=False)),
                ('informacion', models.CharField(max_length=200)),
                ('periodo', models.CharField(max_length=20)),
                ('prerrequisito', models.CharField(blank=True, max_length=50)),
                ('correquisito', models.CharField(blank=True, max_length=50)),
                ('unidad_organ', models.CharField(max_length=20)),
                ('horas_docencia', models.IntegerField()),
                ('horas_prac_docente', models.IntegerField()),
                ('horas_pract_autonoma', models.IntegerField()),
                ('horas_trab_autonomo', models.IntegerField()),
                ('objetivo_general', models.CharField(blank=True, max_length=50)),
                ('id_asignatura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.asignatura')),
                ('id_carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.carrera')),
                ('id_ver_syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.syllabus')),
            ],
        ),
        migrations.AddField(
            model_name='asignatura',
            name='id_carrera',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.carrera'),
        ),
        migrations.CreateModel(
            name='AporteTeorico',
            fields=[
                ('id_aporte_teorico', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('detalle', models.CharField(max_length=500)),
                ('id_ver_syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.syllabus')),
            ],
        ),
        migrations.CreateModel(
            name='AportePerfil',
            fields=[
                ('id_aporte_perfil', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('detalle', models.CharField(max_length=500)),
                ('id_ver_syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.syllabus')),
            ],
        ),
        migrations.CreateModel(
            name='AmbienteAprendizaje',
            fields=[
                ('id_ambiente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('detalle', models.CharField(max_length=500)),
                ('id_ver_syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicioApp.syllabus')),
            ],
        ),
    ]
