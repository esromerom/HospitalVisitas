import django_tables2 as tables
from HospitalApp.models import Cama
import itertools

class TablaOcupacion(tables.Table):
    # nomCama = tables.Column()
    class Meta:
        fields = ['nombre', 'iddependencia__nombres', 'ocupacion']
        model = Cama


    def __init__(self, *args, **kwargs):
        super(TablaOcupacion, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return '%d' % next(self.counter)

    def render_id(self, value):
        return '<%s>' % value