import django_filters
from HospitalApp.models import Dependencia, Asistencia, Cama, Visitante
from django import forms
from django.db import models
from  HospitalApp import filter_extra
import django_bootstrap3_daterangepicker.widgets as widgets

# def dependencias(request):
#     if request is None:
#         return Asistencia.objects.none()
#
#     dependencia = request.identificacion.iddependencia.nombres
#     return dependencia.nombres.all()

class FiltroPrueba1(django_filters.FilterSet):
    dependencias = {}
    dependencia = django_filters.ModelChoiceFilter(queryset=dependencias)

    class Meta:
        model = Asistencia
        fields = ['identificacion__idcama__nombre', 'identificacion__iddependencia__nombres',
                  'identificacion__idcama__ocupacion', 'identificacion__nombre',
                  'identificacion__asistencia__numeromenores']

class DateInput(forms.DateInput):
    input_type = 'date'

class FiltroPrueba2(django_filters.FilterSet):
    dependencia = django_filters.ModelChoiceFilter(queryset=Dependencia.objects.all(),
                                                   field_name='identificacion__iddependencia__nombres',
                                                   label='Dependencia')
    identificacion__idcama = django_filters.ModelChoiceFilter(queryset=Cama.objects.all(),
                                                              label='Cama'
                                                              )
    identificacion__nombre = django_filters.CharFilter(lookup_expr='icontains',label='Nombre',)
    identificacion = django_filters.NumberFilter(lookup_expr='exact', label='Numero de Cedula')
    # fecha = django_filters.DateRangeFilter(widget=widgets.DateRangeWidget(picker_options={
    #     'ranges': widgets.common_dates()}))
    # fecha = filter_extra.DateRangeFilter(label='Date Range')
    # fecha = django_filters.DateFromToRangeFilter(field_name='fechahorainicio',
    #                                              label='Fecha(AAAA-MM-DD)',
    #                                              lookup_expr='icontains',
    #                                              )
    rango = django_filters.DateRangeFilter(field_name='fechahorainicio',
                                           label='Fecha (Rango)',
                                           )
    fechahorainicio__gte = django_filters.DateTimeFilter(widget = DateInput(attrs={'class': 'datepicker'}),
                                      field_name='fechahorainicio',
                                      label='Fecha (Desde)',
                                      lookup_expr='gte'
                                      )
    fechahorafin__lte = django_filters.DateTimeFilter(widget = DateInput(attrs={'class': 'datepicker'}),
                                      field_name='fechahorainicio',
                                      label='Fecha (Hasta)',
                                      lookup_expr='lt'
                                      )


    class Meta:
        model = Asistencia
        fields = {'identificacion__nombre':[],
                  'identificacion__idcama':[],
                  # 'fechahorainicio':['range'],
                  }

    @classmethod
    def filter_for_lookup(cls, f, lookup_type):
        # override date range lookups
        if isinstance(f, models.DateField) and lookup_type == 'range':
            return django_filters.DateRangeFilter, {}

        # use default behavior otherwise
        return super().filter_for_lookup(f, lookup_type)