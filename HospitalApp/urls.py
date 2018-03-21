from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^Servicios/$', views.servicios),
    url(r'^Servicios/Reportes/$', views.reportes),
    # url(r'^Servicios/Admin/$', views.visitas),
    url(r'^home/$', views.home),
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'HospitalApp/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'HospitalApp/logout.html'}),
    url(r'^registro_operario/$', views.registro, name='registro')
]