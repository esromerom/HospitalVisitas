from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from HospitalApp.views import DependenciaView
from HospitalApp.views import TorreView
from HospitalApp.views import HabitacionView
from HospitalApp.views import CamaView
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
    url(r'^Servicios/admin/FormulariosHabitaciones/$', HabitacionView.as_view(), name='formulariohabitacion'),
    url(r'^Servicios/admin/FormulariosCamas/$', CamaView.as_view(), name='formulariocama'),
    url(r'^Servicios/admin/FormularioDependencias$', DependenciaView.as_view(), name='formulariodependencia'),
    url(r'^Servicios/admin/AdministrarCama', views.ConsultaCamaView, name='administrarcama'),
    # url(r'^Servicios/admin/AdministrarCama', ConsultaCamaView.as_view(), name='administrarcama'),
    url(r'^Servicios/admin/$', views.admin, name='admin'),
    url(r'^registro_operario/$', views.registro, name='registro'),
    url(r'^Servicios/Reportes/Ocupacion$', views.ReporteOcupacion.as_view(), name='Reportes'),
    url(r'^Servicios/Reportes/Visitantes$', views.ReporteVisitantes.as_view(), name='Reportes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
