import django_tables2 as tables
from HospitalApp.models import Cama, Visitante, Asistencia
import itertools

class TablaOcupacion(tables.Table):

    export_formats = ['csv', 'xls']
    identificacion__iddependencia__nombres = tables.Column(footer='Visitantes adentro:')
    identificacion__idcama__ocupacion = tables.Column(footer=lambda
        table: sum(x['identificacion__idcama__ocupacion'] for x in table.data))

    def __init__(self, *args, **kwargs):
        super(TablaOcupacion, self).__init__(*args, **kwargs)
        self.base_columns['identificacion__idcama__nombre'].verbose_name = ' Cama '
        self.base_columns['identificacion__iddependencia__nombres'].verbose_name = ' Dependencia '
        self.base_columns['identificacion__idcama__ocupacion'].verbose_name = 'Ocupación'
        self.base_columns['identificacion__nombre'].verbose_name = 'Visitante'
        self.base_columns['identificacion__asistencia__numeromenores'].verbose_name = 'N. Menores'
        self.base_columns['fechahorainicio'].verbose_name = 'Fecha de ingreso'

    class Meta:
        fields = ['identificacion__idcama__nombre',
                  'identificacion__iddependencia__nombres',
                  'identificacion__idcama__ocupacion',
                  'identificacion__nombre',
                  'identificacion__asistencia__numeromenores',
                  'fechahorainicio']
        model = Asistencia
        # sequence = ['nomCama','nomDependencia',
        #             'ocupacion', 'identificacion__nombre',
        #             'numeromenores']
        template = 'django_tables2/bootstrap.html'


class SummingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return sum(bound_column.accessor.resolve(row) for row in table.data)


class TablaVisitantes(tables.Table):
    export_formats = ['csv', 'xls']
    identificacion = tables.Column(accessor='identificacion.idvisitante',
                                   verbose_name='Documento de identidad',
                                   )
    nombre = tables.Column(accessor='identificacion.nombre',
                           verbose_name='Visitante')
    dependencia = tables.Column(accessor='idcama.iddependencia.nombres',
                                verbose_name='Dependencia')
    cama = tables.Column(accessor='idcama.nombre')
    def __init__(self, *args, **kwargs):
        super(TablaVisitantes, self).__init__(*args, **kwargs)
        # self.base_columns['identificacion__idcama__nombre'].verbose_name = ' Cama '
        # self.base_columns['identificacion__iddependencia__nombres'].verbose_name = ' Dependencia '
        # self.base_columns['identificacion__nombre'].verbose_name = ' Nombre Visitante '
        # self.base_columns['identificacion'].verbose_name = ' Documento de Identidad '
        self.base_columns['fechahorainicio'].verbose_name = ' Fecha-Hora Entrada '
        self.base_columns['fechahorafin'].verbose_name = ' Fecha-Hora Salida '
        self.base_columns['estado'].verbose_name = ' Estado '

    class Meta:
        model = Asistencia
        fields = ['fechahorainicio',
                  'fechahorafin',
                  'estado']
        sequence = ('identificacion','nombre','dependencia',
                    'cama', 'estado',
                    'fechahorainicio', 'fechahorafin')
        template = 'django_tables2/bootstrap.html'
