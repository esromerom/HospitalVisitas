import django_filters
from HospitalApp.models import Dependencia, Asistencia, Visitante

class FiltroPrueba(django_filters.FilterSet):
    # nombres = django_filters.ModelChoiceFilter(queryset=Dependencia.objects.values_list('nombres', flat=True))
    nombres = django_filters.ModelChoiceFilter(queryset=Dependencia.objects.all())
    class Meta:
        model = Dependencia
        # fields = ['identificacion__nombre',]
        fields = {'nombres': ['exact', 'iexact'], }


class FiltroVisitantes(django_filters.FilterSet):
    # nombre = django_filters.CharFilter(lookup_expr='iexact')
    # nombre_cont = django_filters.NumberFilter(name='nombre', lookup_expr='icontains')
    #
    # entrada = django_filters.NumberFilter(name='fechahorainicio', lookup_expr='fecha')
    # release_year__gt = django_filters.NumberFilter(name='release_date', lookup_expr='year__gt')
    # release_year__lt = django_filters.NumberFilter(name='release_date', lookup_expr='year__lt')
    #
    # manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Asistencia
        # los que se listan en fields generan un fltro automatico por exacta correpondencia
        fields = {
            'identificacion': ['exact'],
            'identificacion__nombre': ['iexact', 'icontains'],
        }


def dependencias(request):
    if request is None:
        return Dependencia.objects.none()

    nombres = request.identificacion.iddependencia
    return nombres.dependencia_set.all()


class FiltroDependencia(django_filters.FilterSet):
    dependencia = django_filters.ModelChoiceFilter(queryset=Dependencia.objects.all())
    # class Meta:
    #     model = Dependencia
    #     fields = {'nombres': ['iexact', 'icontains']}