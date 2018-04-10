from django.conf.urls import url
from . import views
from django_filters.views import FilterView
from django.contrib.auth.views import login, logout
from HospitalApp.views import CrearDependenciaView, EditarDependenciaView
from HospitalApp.views import TorreView
from HospitalApp.views import CrearHabitacionView
from HospitalApp.views import CrearCamaView
from HospitalApp.views import ReporteOcupacion

from HospitalApp.tablas import TablaOcupacion
from HospitalApp.models import Asistencia
from HospitalApp.filtros import FiltroVisitantes
from HospitalApp.views import ConsultaCamaView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^Servicios/$', views.servicios),
    url(r'^Servicios/Reportes/$', views.menuReportes, name='menuReportes'),
    # url(r'^Servicios/Admin/$', views.visitas),
    # url(r'^home/$', views.home),
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'HospitalApp/login.html'}),
    #url(r'^login/', views.my_view, name='login'),
    url(r'^logout/$', logout, {'template_name': 'HospitalApp/logout.html'}),
    url(r'^Servicios/admin/FormulariosTorres/$', TorreView.as_view(), name='formulariotorre'),

    # Correspondiente a los formularios Habitación
    url(r'^Servicios/admin/FormularioHabitaciones/$', views.HabitacionView, name='formulariohabitacion'),
    url(r'^Servicios/admin/FormularioHabitaciones/Crear/$', CrearHabitacionView.as_view(), name='crearhabitacion'),
    url(r'^Servicios/admin/FormularioHabitaciones/Editar/$', views.EditarHabitacionView, name='editarhabitacion'),
    # url(r'^Servicios/admin/FormularioHabitaciones/Borrar/$', views.BorrarHabitacionView, name='borrarhabitacion'),

    # Correspondiente a los formlarios Cama
    url(r'^Servicios/admin/FormularioCamas/$', views.CamaView, name='formulariocama'),
    url(r'^Servicios/admin/FormularioCamas/Crear/$', views.CrearCamaView, name='crearcama'),
    url(r'^Servicios/admin/FormularioCamas/Editar/$', views.EditarCamaView, name='editarcama'),

    # Correspondiente a los formularios Dependecia
    url(r'^Servicios/admin/FormularioAreas/$', views.DependenciaView, name='formulariodependencia'),
    url(r'^Servicios/admin/FormularioAreas/Crear/$', CrearDependenciaView.as_view(), name='creardependencia'),
    url(r'^Servicios/admin/FormularioAreas/Editar/$', views.EditarDependenciaView, name='editardependencia'),


    url(r'^Servicios/admin/AdministrarCama/', views.ConsultaCamaView, name='administrarcama'),
    # url(r'^Servicios/admin/AdministrarCama', ConsultaCamaView.as_view(), name='administrarcama'),
    url(r'^Servicios/admin/$', views.admin, name='admin'),
    url(r'^Servicios/admin/registro_operario/', views.register, name = 'register'),
    url(r'^Servicios/Reportes/Ocupacion/$',ReporteOcupacion.as_view(),
        name='ReporteOcupación'),

    url(r'^Servicios/Reportes/Visitantes/$', views.ReporteVisitantes.as_view(), name='ReporteVisitantes', ),
    url(r'^Servicios/Reportes/Visitantes/csv/$', views.ReporteExporteVisitantesView.as_view(), name='ExporteReporte', ),
    #url(r'^prueba$', views.ReportePrueba1.as_view(), name="Prueba Filtro"),
]


