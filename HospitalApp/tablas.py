import django_tables2 as tables
from HospitalApp.models import Cama

class TablaOcupacion(tables.Table):
    class Meta:
        model = Cama