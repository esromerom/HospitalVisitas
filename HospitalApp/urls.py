from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from HospitalApp.views import Homeview
from HospitalApp.views import TorreView
from HospitalApp.views import HabitacionView
from HospitalApp.views import CamaView

urlpatterns = [
    url(r'^Servicios/$', views.servicios),
    url(r'^Servicios/Reportes/$', views.reportes.as_view(), name='Reportes'),
    # url(r'^Servicios/Admin/$', views.visitas),
    url(r'^home/$', views.home),
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'HospitalApp/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'HospitalApp/logout.html'}),
    url(r'^Servicios/Formularios/$', Homeview.as_view(), name='formulario'),
    url(r'^Servicios/FormulariosTorres/$', TorreView.as_view(), name='formulariotorre'),
    url(r'^Servicios/FormulariosHabitaciones/$', HabitacionView.as_view(), name='formulariohabitacion'),
    url(r'^Servicios/FormulariosCamas/$', CamaView.as_view(), name='formulariocama'),
    url(r'^registro_operario/$', views.registro, name='registro')
]