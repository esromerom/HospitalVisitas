from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve
from django.views.generic import TemplateView
from HospitalApp.forms import HomeForm
from HospitalApp.forms import Torres
from HospitalApp.forms import Habitaciones
from HospitalApp.forms import Camas
from HospitalApp.models import Cama, Dependencia, Habitacion, Torre, Visitante, Asistencia
from django.shortcuts import render, redirect
from django.forms import forms
import django
from HospitalApp.forms import FormReporteOcupacion
from HospitalApp.tablas import TablaOcupacion, TablaVisitantes
from django_tables2 import RequestConfig, SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django_tables2.export.export import TableExport
from HospitalApp.filtros import FiltroPrueba1, FiltroPrueba2

from datetime import datetime


def ReportePrueba2(request):
    lista = Asistencia.objects.all()
    filtro = FiltroPrueba2(request.GET, queryset=lista)
    print (filtro)
    return render(request, 'HospitalApp/PruebaFiltro.html', {'filter': filtro   })

# SingleTableMixin, FilterView
class ReportePrueba1(SingleTableMixin, FilterView):
    table_class = TablaVisitantes
    model = Asistencia
    template_name = "HospitalApp/PruebaFiltro.html"
    filterset_class = FiltroPrueba2

    def get_queryset(self, **kwargs):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReportePrueba1, self).get_context_data(**kwargs)
        filter = self.filterset_class(self.request.GET, queryset=self.get_queryset(**kwargs))
        # filter.form.helper = FooFilterFormHelper()
        table = self.table_class(filter.qs)
        RequestConfig(self.request,paginate={"per_page": 5, "page": 1}).configure(table)
        context['filter'] = filter
        context['tabla'] = table
        return context




class Homeview(TemplateView):
    template_name = 'HospitalApp/Formularios.html'
    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['nombres']
            form = HomeForm()
            return redirect('formulario')
        else:
            return redirect('formulario')
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


class TorreView(TemplateView):
    template_name = 'HospitalApp/FormularioTorres.html'
    def get(self, request):
        form = Torres()
        return render(request, self.template_name,{'form': form})
    def post(self, request):
        form = Torres(request.POST)
        text = ''
        if form.is_valid():
            form.save()
            text = form.cleaned_data['nombre']
            form = Torres()
            return  redirect('formulariotorre')
        # else:
        #     return redirect('formulariotorre')
        args = {'form':form, 'text': text}
        return render(request, self.template_name, args)


class HabitacionView(TemplateView):
    template_name = 'HospitalApp/FormularioHabitaciones.html'

    def get(self, request):
        form = Habitaciones
        return render(request, self.template_name,{'form': form})
    def post(self, request):
        form = Habitaciones(request.POST)
        text = ''
        if form.is_valid():
            form.save()
            text = form.cleaned_data['nombrehabitacion']
            form = Torres()
            return  redirect('formulariohabitacion')
        args = {'form':form, 'text': text}
        return render(request, self.template_name, args)


class CamaView(TemplateView):
    template_name = 'HospitalApp/FormularioCamas.html'
    def get(self, request):
        form = Camas()
        return render(request, self.template_name,{'form': form})
    def post(self, request):
        form = Camas(request.POST)
        if form.is_valid():
            nr = form.save()
            nr.disponibilidad = nr.iddependencia.cupo
            nr.ocupacion = 0
            nr.save()
            text = form.cleaned_data['nombre']
            # form = Camas()
            return  redirect('formulariocama')
        else:
            return redirect('formulariocama')
        args = {'form':form, 'text': text}
        return render(request, self.template_name, args)


def home(request):
    return render(request, 'HospitalApp/homeHospital.html')


def admin(request):
    return render(request, 'HospitalApp/menuFormularios.html')


def servicios(request):
    return render(request, 'HospitalApp/Servicios.html')


def registro(request):
    current_url = resolve(request.path_info).url_name

    if request.method == 'POST':
        form = OperarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Hospital/login')
            # return render(request, 'HospitalApp/RegistroOpera.html')
            # def login(request):
            #     return render(request, 'HospitalApp/login.html')
    else:
        form = OperarioForm()
        args = {'form': form}
        return render(request, 'HospitalApp/RegistroOpera.html', args)


def visitas(request):
    return render(request, 'HospitalApp/RegistroVisitas.html')


class ReporteOcupacion(ExportMixin, FilterView, SingleTableView):
    table_class = TablaOcupacion
    model = Asistencia
    template_name = "HospitalApp/ReporteOcupacion.html"
    filterset_class = FiltroPrueba2

    def get_table_data(self):
        return self.object_list


    def get(self, request):
        form = FormReporteOcupacion()
        totalCamas = Cama.objects.filter(ocupacion__gt=0).count()
        visitantes_adentro = Asistencia.objects.filter(estado='E')
        totalVisitantes = len(visitantes_adentro)
        # visitas = Asistencia.objects.filter(fechahorafin__day=)
        tabla = TablaOcupacion(visitantes_adentro.values('identificacion__idcama__nombre',
                                                         'identificacion__iddependencia__nombres',
                                                         'identificacion__idcama__ocupacion',
                                                         'identificacion__nombre',
                                                         'identificacion__asistencia__numeromenores'))


        config = RequestConfig(request, paginate={"per_page": 25, "page": 1}).configure(tabla)
        export_format = request.GET.get('_export', 'CSV')
        if TableExport.is_valid_format(export_format):
            ahora = datetime.now()
            fecha = ahora.strftime("%d-%m-%Y")
            exporter = TableExport(export_format, tabla)
            return exporter.response('Visitantes al cierre '+fecha+'.{}'.format(export_format))
        args = {'tabla': tabla, 'forms': form,
                'totalCamas': totalCamas,
                'totalVisitantes': totalVisitantes,
                }

        return render(request, self.template_name, args)



# class ReporteVisitantes(SingleTableMixin, FilterView, TemplateView):

class ReporteVisitantes(SingleTableMixin, FilterView):
    table_class = TablaVisitantes
    model = Asistencia
    template_name = "HospitalApp/ReporteVisitantes.html"
    filterset_class = FiltroPrueba2

    def get_queryset(self, **kwargs):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReporteVisitantes, self).get_context_data(**kwargs)
        filter = self.filterset_class(self.request.GET, queryset=self.get_queryset(**kwargs))
        # filter.form.helper = FooFilterFormHelper()
        table = self.table_class(filter.qs)
        RequestConfig(self.request, paginate={"per_page": 5, "page": 1}).configure(table)
        context['filter'] = filter
        context['tabla'] = table
        return context


class ReporteFiltradoOcupacion(ReporteOcupacion):
    pass

def menuReportes(request):
    return render(request, 'HospitalApp/menuReportes.html')