from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve
from HospitalApp.formularios import OperarioForm
# Create your views here.

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






























