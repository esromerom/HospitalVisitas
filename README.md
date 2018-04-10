# HospitalVisitas
Aplicativo Web para controlar acceso de visitante s aun Hospital
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

class Meta:
    fields = ['identificacion__idcama__nombre',
              'identificacion__iddependencia__nombres',
              'identificacion__idcama__ocupacion',
              'identificacion__nombre',
              'identificacion__asistencia__numeromenores']
    model = Asistencia
    # sequence = ['nomCama','nomDependencia',
    #             'ocupacion', 'identificacion__nombre',
    #             'numeromenores']
    template = 'django_tables2/bootstrap.html'
