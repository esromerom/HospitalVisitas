from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve
from django.views.generic import TemplateView
from HospitalApp.forms import Dependecias
from HospitalApp.forms import Torres
from HospitalApp.forms import Habitaciones
from HospitalApp.forms import Camas
from HospitalApp.forms import ConsultaCamas
from HospitalApp.models import Cama, Dependencia, Habitacion, Torre, Visitante, Asistencia
from django.shortcuts import render, redirect
from django.forms import forms
from HospitalApp.forms import ReporteOcupacion
from HospitalApp.tablas import TablaOcupacion
from django_tables2 import RequestConfig
from django_tables2.export.views import ExportMixin
from django_tables2.export.export import TableExport
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.

class DependenciaView(TemplateView):
    template_name = 'HospitalApp/FormularioDependencia.html'
    def get(self, request):
        form = Dependecias()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = Dependecias(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['nombres']
            form = Dependecias()
            return redirect('formulariodependencia')
        else:
            return redirect('formulariodependencia')
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


class TorreView(TemplateView):
    template_name = 'HospitalApp/FormularioTorres.html'
    def get(self, request):
        form = Torres()
        return render(request, self.template_name,{'form': form})
    def post(self, request):
        form = Torres(request.POST)
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

"""class ConsultaCamaView(TemplateView):
    template_name = 'HospitalApp/AdministrarCamas.html'
    def get(self, request):
        form = ConsultaCamas()
        return render(request, self.template_name,{'form': form})
    def post(self, request):
        form = ConsultaCamas(request.POST)
        if form.is_valid():
            nr = form.save()
            nr.disponibilidad = nr.iddependencia.cupo
            nr.ocupacion = 0
            nr.save()
            text = form.cleaned_data['nombre']
            form = ConsultaCamas()
            return  redirect('administrarcama')
        else:
            return redirect('administrarcama')
        args = {'form':form, 'text': text}
        return render(request, self.template_name, args)"""


def ConsultaCamaView(request):
    if request.method == 'POST':
        form = ConsultaCamas(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print ("AQUI !!!!!  --->>>  ",cd['nombre'].idcama)
            camaReiniciar = Cama.objects.get(idcama=cd['nombre'].idcama) #id or pk or whatever you want
            print ("AQUI !!!!!  --->>>  ",camaReiniciar)
            camaReiniciar.ocupacion = 0
            camaReiniciar.save()
    form = ConsultaCamas()
    return render(request, 'HospitalApp/AdministrarCamas.html', {
        'item': Cama.objects.all(),
        'form' : form,
        })

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


class ReporteOcupacion(ExportMixin, TemplateView):
    template_name = "HospitalApp/ReporteOcupacion.html"
    def get(self, request):
        forms = ReporteOcupacion
        totalCamas = Cama.objects.filter(ocupacion__gt=0).count()
        visitantes_adentro = Asistencia.objects.filter(estado='E')

        totalVisitantes = len(visitantes_adentro)
        tabla = TablaOcupacion(visitantes_adentro.values('identificacion__idcama__nombre',
                                                         'identificacion__iddependencia__nombres',
                                                         'identificacion__idcama__ocupacion',
                                                         'identificacion__nombre',
                                                         'identificacion__asistencia__numeromenores'))
        config = RequestConfig(request).configure(tabla)
        export_format = request.GET.get('_export', 'CSV')
        if TableExport.is_valid_format(export_format):
            ahora = datetime.now()
            fecha = ahora.strftime("%d-%M-%Y")
            exporter = TableExport(export_format, tabla)
            return exporter.response('Visitantes al cierre '+fecha+'.{}'.format(export_format))
        args = {'tabla': tabla, 'forms': forms,
                'totalCamas': totalCamas,
                'totalVisitantes': totalVisitantes,
                }

        return render(request, self.template_name, args)

    def post(self, request):
        pass


class ReporteVisitantes(TemplateView):
    template_name = "HospitalApp/ReporteOcupacion.html"

    def get(self, request):
        forms = ReporteOcupacion
        camas = Cama.objects.filter(ocupacion__gt=0)
        totalCamas = len(camas)
        totalVisitantes = sum(Cama.objects.filter(ocupacion__gt=0).values_list('ocupacion', flat=True))

        tabla = TablaOcupacion(camas.values('nombre', 'iddependencia__nombres', 'ocupacion'))
        args = {'camas': camas, 'tabla': tabla, 'forms': forms,
                'totalCamas': totalCamas, 'totalVisitantes': totalVisitantes}

        return render(request, self.template_name, args)

    def post(self, request):
        pass

def menuReportes(request):
    return render(request, 'HospitalApp/menuReportes.html')