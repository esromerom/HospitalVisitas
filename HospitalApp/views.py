from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
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
    if request == 'POST':
        form = UserCreationForm(request)
    # return render(request, 'HospitalApp/RegistroOpera.html')
# def login(request):
#     return render(request, 'HospitalApp/login.html')