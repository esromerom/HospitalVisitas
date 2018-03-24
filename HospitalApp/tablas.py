import django_tables2 as tables
from HospitalApp.models import Cama, Visitante, Asistencia
import itertools

class TablaOcupacion(tables.Table):
    # nomCama = tables.Column()
    export_formats = ['csv', 'xls']
    def __init__(self, *args, **kwargs):
        super(TablaOcupacion, self).__init__(*args, **kwargs)
        self.base_columns['identificacion__idcama__nombre'].verbose_name = ' Cama '
        self.base_columns['identificacion__iddependencia__nombres'].verbose_name = ' Dependencia '
        self.base_columns['identificacion__idcama__ocupacion'].verbose_name = 'Ocupación'
        self.base_columns['identificacion__nombre'].verbose_name = 'Visitante'
        self.base_columns['identificacion__asistencia__numeromenores'].verbose_name = 'N. Menores'

    class Meta:
        fields = ['identificacion__idcama__nombre', 'identificacion__iddependencia__nombres',
                  'identificacion__idcama__ocupacion', 'identificacion__nombre',
                  'identificacion__asistencia__numeromenores']
        model = Asistencia
        template = 'django_tables2/bootstrap.html'


class SummingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return sum(bound_column.accessor.resolve(row) for row in table.data)


class TablaVisitantes(tables.Table):
    # nomCama = tables.Column()
    Dependencia = tables.Column(footer='Total:')
    export_formats = ['csv', 'xls']
    # ocupacion = SummingColumn()
    def __init__(self, *args, **kwargs):
        super(TablaVisitantes, self).__init__(*args, **kwargs)
        self.base_columns['nombre'].verbose_name = ' Cama '
        self.base_columns['iddependencia__nombres'].verbose_name = ' Dependencia '
        self.base_columns['ocupacion'].verbose_name = ' Ocupación '
        self.base_columns['iddependencia__visitante__nombre'].verbose_name = ' Visitante '

    class Meta:
        fields = ['nombre', 'iddependencia__nombres', 'ocupacion']
        model = Visitante
        row_attrs = {'data-id': lambda record: record.pk}
        localize = ('nombre',)
        template = 'django_tables2/bootstrap.html'
