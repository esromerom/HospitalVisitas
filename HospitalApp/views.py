from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve
from django.views.generic import TemplateView
from django.views.generic import TemplateView
from HospitalApp.models import Cama, Dependencia, Habitacion, Torre, Asistencia
from HospitalApp.forms import HomeForm
from HospitalApp.forms import Torres
from HospitalApp.forms import Habitaciones
from HospitalApp.forms import Camas
from HospitalApp.models import Cama, Dependencia, Habitacion, Torre
from django.shortcuts import render, redirect
from django.forms import forms
from HospitalApp.forms import ReporteOcupacion
from HospitalApp.tablas import TablaOcupacion
from django_tables2 import RequestConfig


# Create your views here.

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


class Ocupacion(TemplateView):
    template_name = "HospitalApp/ReporteOcupacion.html"
    def get(self, request):
        forms = ReporteOcupacion
        camas = Cama.objects.filter(ocupacion__gt=0)
        totalCamas = len(camas)
        totalVisitantes = sum(Cama.objects.filter(ocupacion__gt=0).values_list('ocupacion',flat=True))

        tabla = TablaOcupacion(camas.values('nombre', 'iddependencia__nombres', 'ocupacion'))
        args = {'camas': camas, 'tabla': tabla, 'forms': forms,
                'totalCamas': totalCamas, 'totalVisitantes': totalVisitantes}

        return render(request, self.template_name, args)

    def post(self, request):
        pass

def menuReportes(request):
    return render(request, 'HospitalApp/menuReportes.html')