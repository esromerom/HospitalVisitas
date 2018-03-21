from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve
from django.views.generic import TemplateView
from HospitalApp.forms import HomeForm
from HospitalApp.forms import Torres
from HospitalApp.forms import Habitaciones
from HospitalApp.forms import Camas
from HospitalApp.models import Cama
from django.shortcuts import render, redirect


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



def reportes(request):
    casos = ['VisArea', 'xID', 'xDia', 'xMes', 'xIntervalo', 'xNombre', 'xServicio', 'xCierre']
    Texto = ['Reporte de Número de Visitantes por Area',
             'Reporte de Visitante por ID',
             'Reporte de visitantes por Día',
             'Reporte de Visitantes por mes',
             'Reporte de Visitantes por Intervalos de Tiempo',
             'Reporte de Visitantes por Nombre',
             'Reporte de Visitantes por Servicio'
             'Reporte de Visitantes al cierre']
    reportesCasos = {}
    # reportesCasos.keys(casos)
    # reportesCasos.values(Texto)
    return render(request, 'HospitalApp/Reporte.html')


def home(request):
    return render(request, 'HospitalApp/homeHospital.html')


def servicios(request):
    return render(request, 'HospitalApp/Servicios.html')


def registro(request):
    current_url = resolve(request.path_info).url_name
    print (current_url)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Hospital/login')
            # return render(request, 'HospitalApp/RegistroOpera.html')
            # def login(request):
            #     return render(request, 'HospitalApp/login.html')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'HospitalApp/RegistroOpera.html', args)
