from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from django.utils import timezone


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('principal')
        else:
            error_message = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
            return render(request, 'inicio.html', {'error_message': error_message})
    else:
        return render(request, 'inicio.html')


@login_required
def guardar_informacion(request):
    if request.method == 'POST':
        # Verificar que el usuario esté autenticado
        if not request.user.is_authenticated:
            return redirect('login')  # Si el usuario no está autenticado, redirigir al formulario de login

        # Obtener los datos del formulario
        carrera = request.POST.get('carrera')
        informacion = request.POST.get('informacion')
        asignatura_id = request.POST.get('id_asignatura')
        periodo = request.POST.get('periodo')
        prerrequisito = request.POST.get('prerrequisito')
        correquisito = request.POST.get('correquisito')
        unidad_organ = request.POST.get('unidad_organ')
        profesional = request.POST.get('profesional')
        horas_docencia = request.POST.get('horas_docencia')
        horas_prac_docente = request.POST.get('horas_prac_docente')
        horas_pract_autonoma = request.POST.get('horas_pract_autonoma')
        horas_trab_autonomo = request.POST.get('horas_trab_autonomo')
        try:
            asignatura_obj = asignatura.objects.get(id_asignatura=asignatura_id)
        except asignatura.DoesNotExist:
            asignatura_obj = None

        # Crear un nuevo objeto Informativo y asignar el usuario logeado
        informativo = Informativo.objects.create(
            carrera=carrera,
            informacion=informacion,
            id_asignatura=asignatura_obj,
            periodo=periodo,
            prerrequisito=prerrequisito,
            correquisito=correquisito,
            unidad_organ=unidad_organ,
            profesional=profesional,
            horas_docencia=horas_docencia,
            horas_prac_docente=horas_prac_docente,
            horas_pract_autonoma=horas_pract_autonoma,
            horas_trab_autonomo=horas_trab_autonomo,
            id_ver_syllabus=None,  # Asegúrate de proporcionar el id_ver_syllabus adecuado si es necesario
            id_usuario=request.user,  # Asignar el usuario logeado al campo id_usuario
        )

        # Guardar el objeto Informativo en la base de datos
        informativo.save()

        # Obtener todos los objetos Informativo relacionados con el usuario logeado
        informativos_usuario = Informativo.objects.filter(id_usuario=request.user)

        return render(request, 'materia.html', {'informativos': informativos_usuario})

@login_required
def borrar_informacion(request, id_informativo):
    # Verificar que el usuario esté autenticado
    if not request.user.is_authenticated:
        return redirect('login')  # Si el usuario no está autenticado, redirigir al formulario de login

    # Obtener el objeto Informativo que se desea eliminar
    informativo = get_object_or_404(Informativo, pk=id_informativo, id_usuario=request.user)

    # Eliminar el objeto Informativo de la base de datos
    informativo.delete()

    # Redirigir a la página donde se muestran las asignaturas del usuario logueado
    return redirect('materia')
@login_required
def ensenar_informacion(request):
    informativos_usuario = Informativo.objects.filter(id_usuario=request.user)
    return render(request, 'materia.html', {'informativos': informativos_usuario})

@login_required
def ensenar_informacion2(request):
    informativos_usuario = Informativo.objects.filter(id_usuario=request.user)

    # Combinar los dos diccionarios en uno solo para pasarlos al contexto
    context = {
        'informativos': informativos_usuario,
    }
    return render(request, 'plan.html', context)


def guardar_informacion2(request):
    if request.method == 'POST':
        # Obtener el último objeto Informativo creado (el recién guardado)
        informativo = Informativo.objects.last()

        # Crear un nuevo objeto Syllabus y guardar en la base de datos
        nombre_syllabus = informativo.id_asignatura
        fecha_creacion_syllabus = timezone.now()  # O la fecha que desees
        version_syllabus = "1.0"  # O la versión que desees

        syllabus = Syllabus.objects.create(
            nombre=nombre_syllabus,
            fecha_creacion=fecha_creacion_syllabus,
            version=version_syllabus,
            id_usuario=request.user,  # Asignar el usuario logeado al campo id_usuario del Syllabus
        )
        informativo.id_ver_syllabus = syllabus
        informativo.save()


        # Procesar y guardar las Unidades Temáticas
        for i in range(1, 5):  # Ajusta el rango según el número máximo de unidades temáticas
            nombre_unidad = request.POST.get(f'nombre_unidad_{i}')
            objetivo_unidad = request.POST.get(f'objetivo_unidad_{i}')

            unidad = Unidad.objects.create(nombre=nombre_unidad, objetivo=objetivo_unidad, id_ver_syllabus=syllabus)

            # Obtener todas las claves del diccionario request.POST
            keys = request.POST.keys()

            # Filtrar las claves que corresponden a los campos de la unidad actual (i)
            fields = [key for key in keys if key.startswith(f'contenido_unidad{i}_')]

            # Iterar sobre los campos filtrados
            for field in fields:
                # Extraer el número de campo (j) del nombre de la clave
                j = int(field.split('_')[-1])

                # Obtener los valores de los campos para cada j
                contenido_item = request.POST.get(f'contenido_unidad{i}_{j}')
                hora_docencia_item = request.POST.get(f'hora_docencia_unidad{i}_{j}')
                hora_practica_item = request.POST.get(f'hora_practica_unidad{i}_{j}')
                horas_autonomas_item = request.POST.get(f'horas_autonomas_unidad{i}_{j}')

                # Guardar los valores en la base de datos
                ItemUnidad.objects.create(
                    contenido=contenido_item,
                    hora_docencia=hora_docencia_item,
                    hora_practica=hora_practica_item,
                    horas_autonomas=horas_autonomas_item,
                    id_unidad=unidad

                )

        # Procesar y guardar el Ambiente de Aprendizaje
        detalle_ambiente = request.POST.get('detalle_ambiente')

        # Crea un nuevo objeto AmbienteAprendizaje y guarda en la base de datos
        AmbienteAprendizaje.objects.create(
            detalle=detalle_ambiente,
            id_ver_syllabus=syllabus
        )

        detalle_academico = request.POST.get('detalle_academico')
        # Crea un nuevo objeto detalleacademico y guarda en la base de datos
        ProductoAcademicoItem.objects.create(
            detalle=detalle_academico,
            id_ver_syllabus=syllabus
        )

        # Procesar y guardar los Productos Académicos

        for i in range(1, 5):  # Ajusta el rango según el número máximo de productos académicos
            objetivo_prod_academico = request.POST.get(f'objetivo_prod_academico_{i}')
            productos_parciales_prod_academico = request.POST.get(f'productos_parciales_prod_academico_{i}')
            resultados_prod_academico = request.POST.get(f'resultados_prod_academico_{i}')
            integracion_prod_academico = request.POST.get(f'integracion_prod_academico_{i}')

            # Crea un nuevo objeto ProductoAcademico y guarda en la base de datos
            ProductoAcademico.objects.create(
                objetivo=objetivo_prod_academico,
                productos_parciales=productos_parciales_prod_academico,
                resultados=resultados_prod_academico,
                integracion=integracion_prod_academico,
                id_ver_syllabus=syllabus
            )

        # Procesar y guardar las Referencias
        for i in range(1, 3):  # Ajusta el rango según el número de conjuntos de inputs (en este caso, 2 conjuntos)
            basica_referencia = request.POST.get(f'basica_{i}')
            complementaria_referencia = request.POST.get(f'complementaria_{i}')
            sitioweb_referencia = request.POST.get(f'sitioweb_{i}')

            # Crea un nuevo objeto Referencia y guarda en la base de datos
            Referencia.objects.create(
                basica=basica_referencia,
                complementaria=complementaria_referencia,
                sitioweb=sitioweb_referencia,
                id_ver_syllabus=syllabus
            )

        # Redirigir a una página de éxito o cualquier otra página que desees después de guardar los datos
        return redirect('plan')

    # Si el método de solicitud es GET, simplemente mostrar el formulario
    return render(request, 'plan.html')


def ensenar_informacion4(request, informativo_id):
    informativo = get_object_or_404(Informativo, id_informativo=informativo_id, id_usuario=request.user)
    objetivo_especificos = Objetivo_especifico.objects.filter(id_asignatura=informativo.id_asignatura)
    context = {
        'informativos': informativo,
        'objetivo_especifico': objetivo_especificos
    }
    return render(request, 'plan.html', context)

def ensenar_informacion3(request):
    # Obtener el usuario actual
    usuario_actual = request.user

    # Filtrar los Syllabus que pertenecen al usuario actual
    syllabus_usuario = Syllabus.objects.filter(id_usuario=usuario_actual)

    # Filtrar los informativos que tienen uno de los Syllabus asociados al usuario actual
    informativos_usuario = Informativo.objects.filter(id_ver_syllabus__in=syllabus_usuario)

    # Combinar los dos diccionarios en uno solo para pasarlos al contexto
    context = {
        'informativos': informativos_usuario,
    }
    print(f"Total de Syllabus filtrados: {syllabus_usuario.count()}")
    print(f"Total de Informativos filtrados: {informativos_usuario.count()}")
    return render(request, 'version.html', context)

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio.html')


def iniciodef(request):
    return render(request, 'inicio.html', {})
@login_required
def principalDef(request):
    return render(request, 'principal.html', {})
@login_required
def materiaDef(request):
    informativos_usuario = Informativo.objects.filter(id_usuario=request.user)
    return render(request, 'materia.html', {'informativos': informativos_usuario})

def planDef(request):
    informativos_usuario = Informativo.objects.filter(id_usuario=request.user)

    # Combinar los dos diccionarios en uno solo para pasarlos al contexto
    context = {
        'informativos': informativos_usuario,
    }
    return render(request, 'plan.html', context)

@login_required
def versionDef(request):
    # Obtener el usuario actual
    usuario_actual = request.user

    # Filtrar los Syllabus que pertenecen al usuario actual
    syllabus_usuario = Syllabus.objects.filter(id_usuario=usuario_actual)

    # Filtrar los informativos que tienen uno de los Syllabus asociados al usuario actual
    informativos_usuario = Informativo.objects.filter(id_ver_syllabus__in=syllabus_usuario)

    # Combinar los dos diccionarios en uno solo para pasarlos al contexto
    context = {
        'informativos': informativos_usuario,
    }
    return render(request, 'version.html', context)


def pdfDef(request, informativo_id):
    # Obtener el objeto Informativo desde la base de datos usando el ID proporcionado en la URL
    informativo = get_object_or_404(Informativo, id_informativo=informativo_id)
    objetivos_especificos = Objetivo_especifico.objects.filter(id_asignatura=informativo.id_asignatura)
    aportes_teoricos = AporteTeorico.objects.filter(id_asignatura=informativo.id_asignatura)
    aportes_perfil = AportePerfil.objects.filter(id_asignatura=informativo.id_asignatura)

    unidades = Unidad.objects.filter(id_ver_syllabus=informativo.id_ver_syllabus)
    items_unidades = ItemUnidad.objects.filter(id_unidad__id_ver_syllabus=informativo.id_ver_syllabus)
    ambientes_aprendizaje = AmbienteAprendizaje.objects.filter(id_ver_syllabus=informativo.id_ver_syllabus)
    productos_academicosItems = ProductoAcademicoItem.objects.filter(id_ver_syllabus=informativo.id_ver_syllabus)
    productos_academicos = ProductoAcademico.objects.filter(id_ver_syllabus=informativo.id_ver_syllabus)
    referencias = Referencia.objects.filter(id_ver_syllabus=informativo.id_ver_syllabus)
    docentes = Docente.objects.filter(id_asignatura=informativo.id_asignatura)
    docentes2 = Docente2.objects.filter(id_asignatura=informativo.id_asignatura)


    context = {
        'informativo': informativo,
        "objetivo_especifico": objetivos_especificos,
        'aportes_teoricos': aportes_teoricos,
        'aportes_perfil': aportes_perfil,
        'unidades': unidades,
        'items_unidades': items_unidades,
        'ambientes_aprendizaje': ambientes_aprendizaje,
        'productos_academicosItem': productos_academicosItems,
        'productos_academicos': productos_academicos,
        'referencias': referencias,
        'docentes': docentes,
        'docentes2': docentes2
    }

    # Renderizar la plantilla PDF.html con los datos del contexto
    return render(request, 'PDF.html', context)


