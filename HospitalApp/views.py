from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import resolve
from django.views.generic import TemplateView
from HospitalApp.forms import CrearDependecias, EditarDependencias
from HospitalApp.forms import Torres
from HospitalApp.forms import CrearHabitaciones, EditarHabitaciones
from HospitalApp.forms import CrearCamas, EditarCamas
from HospitalApp.forms import ConsultaCamas
from HospitalApp.forms import FormReporteOcupacion
from HospitalApp.models import Cama, Dependencia, Habitacion, Torre, Visitante, Asistencia
from django.shortcuts import render, redirect
from django.forms import forms
import csv
from HospitalApp.tablas import TablaOcupacion, TablaVisitantes
from django_tables2 import RequestConfig, SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from HospitalApp.forms import ConsultaCamas, ConsultaDependencias, ConsultaHabitacion, OperarioForm
from HospitalApp.models import Cama, Dependencia, Habitacion, Torre, Visitante, Asistencia
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.forms import forms
from HospitalApp.forms import FormReporteOcupacion
from HospitalApp.tablas import TablaOcupacion
from django_tables2 import RequestConfig

from django_tables2.export.views import ExportMixin
from django_tables2.export.export import TableExport
from HospitalApp.filtros import  FiltroVisitantes

from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import get_list_or_404, get_object_or_404
from HospitalApp.forms import CreacionUsuario

def ReportePrueba2(request):
    lista = Asistencia.objects.all()
    filtro = FiltroVisitantes(request.GET, queryset=lista)
    print (filtro)
    return render(request, 'HospitalApp/PruebaFiltro.html', {'filter': filtro   })

# SingleTableMixin, FilterView
class ReportePrueba1(SingleTableMixin, FilterView):
    table_class = TablaVisitantes
    model = Asistencia
    template_name = "HospitalApp/PruebaFiltro.html"
    filterset_class = FiltroVisitantes

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


def DependenciaView(request):
    # idd = 1
    # form = ConsultaDependencias()
    # if request.method == 'GET':
    #     form = ConsultaDependencias()
    # elif request.method == 'POST':
    #     form = ConsultaDependencias(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         cd = form.save(commit=False)
    #         idd = form.cleaned_data.get('iddependencia')
    #         print (idd)
    #         print("AQUI !!!!!  --->>>  ", cd['nombres'].iddependencia)
    #
    #         return redirect('administrarcama')
    return render(request, 'HospitalApp/MenuDependencia.html', {
                        'item': Dependencia.objects.all(),
                        # 'form': form,
                        # 'id': idd,
                    })


class CrearDependenciaView(TemplateView):
    template_name = 'HospitalApp/CrearDependencia.html'
    iddependencia = None
    def get(self, request):
        # self.iddependencia = request.session.get('iddependencia', None)
        form = CrearDependecias()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = CrearDependecias(request.POST)
        if form.is_valid():
            form.save()
            form = CrearDependecias()
            r = Dependencia.objects.last()
            r.menores = 3
            r.save()
            # return redirect('formulariodependencia')
        args = {'form': form,}
        # message success
        return render(request, self.template_name, args)


def EditarDependenciaView(request):
    # instance = get_object_or_404(Dependencia,id=iddependencia)
    form = EditarDependencias()
    # if request.method == 'GET':
    #     form = EditarDependecias()
    if request.method == "POST":
        form = EditarDependencias(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print (dir(cd))
            depEditar = Dependencia.objects.get(iddependencia= cd['iddependencia'].iddependencia)
            print ("Aquí -->",depEditar.nombres)
            depEditar.nombres = cd['nombres']
            # depEditar.hora_inicio = cd['hora_inicio']
            # depEditar.hora_fin = cd['hora_fin']
            # depEditar.cupo = cd['cupo']
            depEditar.save()
            return render(request, 'HospitalApp/MenuDependencia.html')
    return render(request, 'HospitalApp/EditarDependencia.html', {
                    'item': Dependencia.objects.all(),
                    'form': form,
                })


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


def HabitacionView(request):
    # idd = 0
    # if request.method == 'GET':
    #     form = ConsultaHabitacion()
    # if request.method == 'POST':
    #     form = ConsultaDependencias(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         cd = form.save()
    #         idd = form.iddependencia
    #
    # form = ConsultaHabitacion()
    return render(request, 'HospitalApp/MenuHabitacion.html', {
                'item': Habitacion.objects.all(),
                # 'form': form,
                # 'iddependencia':idd,
                })


class CrearHabitacionView(TemplateView):
    template_name = 'HospitalApp/FormularioHabitaciones.html'
    def get(self, request):
        form = CrearHabitaciones
        return render(request, self.template_name,{'form': form})
    def post(self, request):
        form = CrearHabitaciones(request.POST)
        text = ''
        if form.is_valid():
            form.save()
            nuevaHab = Habitacion.objects.last()
            #Si termina en número la habitación completa las camas con LETRAS
            if (ord(nuevaHab.nombrehabitacion[-1]) > 47 \
                    and ord(nuevaHab.nombrehabitacion[-1]) <58):
                for cam in range(nuevaHab.ncamas):
                    nuevaCama = Cama()
                    nuevaCama.iddependencia = nuevaHab.iddependencia
                    nuevaCama.nombre = nuevaHab.nombrehabitacion + chr(65+cam)
                    nuevaCama.ocupacion = 0
                    nuevaCama.disponibilidad = nuevaHab.iddependencia.cupo
                    nuevaCama.idhabitacion_id = nuevaHab.idhabitacion
                    nuevaCama.save()
            # Si termina en letra la habitación Completa las camas con 123456
            elif ((ord(nuevaHab.nombrehabitacion[-1]) > 96) and
                      (ord(nuevaHab.nombrehabitacion[-1]) <123)) or \
                    ((ord(nuevaHab.nombrehabitacion[-1]) > 64) and
                         (ord(nuevaHab.nombrehabitacion[-1]) < 91)):
                for cam in range(nuevaHab.ncamas):
                    nuevaCama = Cama()
                    nuevaCama.iddependencia = nuevaHab.iddependencia
                    nuevaCama.nombre = nuevaHab.nombrehabitacion + str(cam+1)
                    nuevaCama.ocupacion = 0
                    nuevaCama.disponibilidad = nuevaHab.iddependencia.cupo
                    nuevaCama.idhabitacion_id = nuevaHab.idhabitacion
                    nuevaCama.save()
            text = form.cleaned_data['nombrehabitacion']
            form = CrearHabitaciones()

            return  redirect('formulariohabitacion')
        args = {'form':form, 'text': text}
        return render(request, self.template_name, args)


def EditarHabitacionView(request):
    # instance = get_object_or_404(Dependencia,id=iddependencia)
    form = EditarHabitaciones()
    # if request.method == 'GET':
    #     form = EditarDependecias()
    if request.method == "POST":
        form = EditarHabitaciones(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            habEditar = Habitacion.objects.get(idhabitacion= cd['idhabitacion'].idhabitacion)
            print ("Aquí -->",habEditar.nombrehabitacion)
            habEditar.nombrehabitacion = cd['nombrehabitacion']
            habEditar.piso = cd['piso']
            habEditar.idtorre = cd['idtorre']
            habEditar.iddependencia = cd['iddependencia']
            habEditar.ncamas = cd['ncamas']
            habEditar.save()
            return render(request, 'HospitalApp/MenuHabitacion.html')
    return render(request, 'HospitalApp/EditarHabitacion.html', {
                    'item': Dependencia.objects.all(),
                    'form': form,
                })


def BorrarHabitacionView(request):
    # instance = get_object_or_404(Dependencia,id=iddependencia)
    form = ConsultaHabitacion()
    # if request.method == 'GET':
    #     form = EditarDependecias()
    if request.method == "POST":
        form = ConsultaHabitacion(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            habBorrar = Habitacion.objects.get(idhabitacion= cd['idhabitacion'].idhabitacion)
            camasBorrar = Cama.objects.filter(idhabitacion= habBorrar.idhabitacion)
            camasBorrar.delete()
            habBorrar.delete()
            return render(request, 'HospitalApp/MenuHabitacion.html')
    return render(request, 'HospitalApp/BorrarHabitacion.html', {
                    'item': Dependencia.objects.all(),
                    'form': form,
                })


def CamaView(request):
    # idd = 0
    # if request.method == 'GET':
    #     form = ConsultaHabitacion()
    # if request.method == 'POST':
    #     form = ConsultaDependencias(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         cd = form.save()
    #         idd = form.iddependencia
    #
    # form = ConsultaHabitacion()
    return render(request, 'HospitalApp/MenuCama.html', {
                'item': Habitacion.objects.all(),
                # 'form': form,
                # 'iddependencia':idd,
                })


def CrearCamaView(request):
    template_name = 'HospitalApp/CrearCama.html'
    form = CrearCamas()
    if request.method == "POST":
        form = CrearCamas(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            camCrear = Cama()
            # nr.iddependencia = cam['idhabitacion'].iddependencia
            camCrear.nombre = cd['nombre']
            camCrear.disponibilidad = cd['disponibilidad']
            camCrear.ocupacion = 0
            camCrear.idhabitacion = cd['idhabitacion'].idhabitacion
            camCrear.iddependencia = Dependencia.objects.get(iddependencia=Habitacion.objects.get(idhabitacion=cd['idhabitacion'].idhabitacion).iddependencia)
            camCrear.save()
            # text = form.cleaned_data['nombre']
            # form = Camas()
            return render(request, 'HospitalApp/MenuCama.html')
    args = {'form':form,
                }
    return render(request, template_name, args)


def EditarCamaView(request):
    template_name = 'HospitalApp/EditarCama.html'
    form = EditarCamas()
    if request.method == "POST":
        form = EditarCamas(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            camEditar = Cama.objects.get(idcama=cd['idcama'].idcama)
            # nr.iddependencia = cam['idhabitacion'].iddependencia
            camEditar.nombre = cd['nombre']
            camEditar.disponibilidad = cd['disponibilidad']
            camEditar.ocupacion = 0
            camEditar.iddependencia = (Dependencia.objects.get(iddependencia=
                                            Habitacion.objects.get(idhabitacion=
                                                    Cama.objects.get(idcama=cd['idcama'].idcama).idhabitacion_id).iddependencia_id))
            camEditar.save()
            # text = form.cleaned_data['nombre']
            # form = Camas()
            return  redirect('formulariocama')
        args = {'form':form,
                }
        return render(request, template_name, args)
    args = {'form': form,
            }
    return render(request, template_name, args)

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
            # cd = form.save()
            print ("AQUI !!!!!  --->>>  ",cd['nombre'].idcama)
            camaReiniciar = Cama.objects.get(idcama=cd['nombre'].idcama) #id or pk or whatever you want
            asistenciaReiniciar = Asistencia.objects.filter(idcama=camaReiniciar.idcama).get(estado="E")
            camaReiniciar.ocupacion = 0
            asistenciaReiniciar.estado = "S"
            camaReiniciar.disponibilidad = camaReiniciar.iddependencia.cupo
            camaReiniciar.save()
            asistenciaReiniciar.save()
            return redirect('administrarcama')
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


class ReporteOcupacion(ExportMixin, FilterView, SingleTableView):
    table_class = TablaOcupacion
    model = Asistencia
    template_name = "HospitalApp/ReporteOcupacion.html"
    # filterset_class = FiltroPrueba2

    def get_table_data(self):
        return self.object_list


    def get(self, request):
        form = FormReporteOcupacion()
        totalCamas = Cama.objects.filter(ocupacion__gt=0).count()
        visitantes_adentro = Asistencia.objects.filter(estado__exact="E")
        totalVisitantes = len(visitantes_adentro)
        tabla = TablaOcupacion(visitantes_adentro.values('idcama__nombre',
                                                         'idcama__iddependencia__nombres',
                                                         'idcama__ocupacion',
                                                         'identificacion__nombre',
                                                         'numeromenores',
                                                         'fechahorainicio'))
        config = RequestConfig(request).configure(tabla)
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
    filterset_class = FiltroVisitantes

    def get_queryset(self, **kwargs):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReporteVisitantes, self).get_context_data(**kwargs)
        filter = self.filterset_class(self.request.GET, queryset=self.get_queryset(**kwargs))
        # filter.form.helper = FooFilterFormHelper()
        table = self.table_class(filter.qs)
        RequestConfig(self.request, paginate={"per_page": 25, "page": 1}).configure(table)
        context['filter'] = filter
        context['tabla'] = table
        # print (table.columns.visible.identificacion)
        return context


class ReporteExporteVisitantesView(FilterView):
    filterset_class = FiltroVisitantes

    def render_to_response(self, context, **response_kwargs):
        # Could use timezone.now(), but that makes the string much longer
        ahora = datetime.now()
        fecha = ahora.strftime("%d-%m-%Y")
        filename = "{}-export.csv".format(fecha)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        writer = csv.writer(response)
        writer.writerow(['Doc. de identidad','Nombre Visitante',
                         # 'Dependencia','Cama',
                         'Entrada/Salida',
                         'Fecha - Hora Entrada', 'Fecha - Hora Salida'])

        for obj in self.object_list:
            writer.writerow([obj.identificacion, obj.identificacion.nombre,
                             # obj.idcama.iddependencia.nombres,
                             # Cama.objects.filter(idcama=obj.idcama.idcama),
                             obj.estado, obj.fechahorainicio, obj.fechahorafin])

        return response


class ReporteFiltradoOcupacion(ReporteOcupacion):
    pass


def menuReportes(request):
    return render(request, 'HospitalApp/menuReportes.html')


def register(request):
    if request.method == 'POST':
        f = CreacionUsuario(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/Hospital/Servicios/')

    else:
        f = CreacionUsuario()

    return render(request, 'HospitalApp/RegistroOpera.html', {'form': f})
