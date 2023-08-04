from .models import asignatura


def asignaturas_context(request):
    asignaturas = asignatura.objects.all()
    return {'asignaturas': asignaturas}
