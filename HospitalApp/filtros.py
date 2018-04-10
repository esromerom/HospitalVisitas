import django_filters
from HospitalApp.models import Dependencia, Asistencia, Cama, Visitante
from django import forms
from django.db import models
from  HospitalApp import filter_extra
import django_bootstrap3_daterangepicker.widgets as widgets
# from django_filters.conf import DEFAULTS
from Hospital.settings import FILTERS_VERBOSE_LOOKUPS

class DateInput(forms.DateInput):
    input_type = 'date'

class FiltroVisitantes(django_filters.FilterSet):
    dependencia = django_filters.ModelChoiceFilter(queryset=Dependencia.objects.all().order_by('nombres'),
                                                   field_name='iddependencia__nombres',
                                                   label=u'Dependencia')
    idcama = django_filters.ModelChoiceFilter(queryset=Cama.objects.all().order_by('nombre'),
                                              field_name='idcama__nombre',
                                              label=u'Cama')
    identificacion__nombre = django_filters.CharFilter(lookup_expr='icontains',label='Nombre',)
    identificacion = django_filters.NumberFilter(lookup_expr='exact', label='Numero de Cedula')
    fechahorainicio = django_filters.DateFilter(widget = DateInput(attrs={'class': 'datepicker'}),
                                      field_name='fechahorainicio',
                                      label='Fecha (Desde)',
                                      lookup_expr='gt'
                                      )
    fechahorafin = django_filters.DateFilter(widget = DateInput(attrs={'class': 'datepicker'}),
                                      field_name='fechahorainicio',
                                      label='Fecha (Hasta)',
                                      lookup_expr=('lte'))


    class Meta:
        model = Asistencia
        fields = {'identificacion__nombre':[],
                  'identificacion__idcama':[],
                  'idcama':[],
                  # 'fechahorainicio':['range'],
                  }
