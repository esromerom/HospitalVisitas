# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asistencia(models.Model):
    idasistencia = models.AutoField(primary_key=True)
    identificacion = models.ForeignKey('Visitante', models.DO_NOTHING, db_column='identificacion')
    idmenor = models.IntegerField(blank=True, null=True)
    dispositivo = models.IntegerField()
    fechahorainicio = models.DateTimeField(blank=True, null=True)
    fechahorafin = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    numeromenores = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    idcama = models.ForeignKey('Cama', models.DO_NOTHING, db_column='idcama')
    iddependencia = models.ForeignKey('Dependencia', models.DO_NOTHING, db_column='iddependencia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cama(models.Model):
    idcama = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45)
    idhabitacion = models.ForeignKey('Habitacion', models.DO_NOTHING, db_column='idhabitacion')
    iddependencia = models.ForeignKey('Dependencia', models.DO_NOTHING, db_column='iddependencia',null=True,blank=True)
    ocupacion = models.PositiveIntegerField(blank=True, null=True)
    disponibilidad = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cama'

    def __str__(self):
        return self.nombre


class Dependencia(models.Model):
    iddependencia = models.AutoField(primary_key=True)
    nombres = models.CharField(unique=True, max_length=45)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    cupo = models.PositiveIntegerField(blank=True, null=True)
    menores = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dependencia'

    def __str__(self):
        return self.nombres

    # def get_absolute_url(self):
    #     return reversed("formulariodependencia", kwargs={"iddependencia": self.iddependencia})

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class Fotos(models.Model):
    idfoto = models.AutoField(primary_key=True)
    identificacion = models.ForeignKey('Visitante', models.DO_NOTHING, db_column='identificacion')
    foto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fotos'


class Habitacion(models.Model):
    idhabitacion = models.AutoField(primary_key=True)
    nombrehabitacion = models.CharField(max_length=45)
    piso = models.CharField(max_length=45)
    idtorre = models.ForeignKey('Torre', models.DO_NOTHING, db_column='idtorre')
    ncamas = models.PositiveIntegerField()
    iddependencia = models.ForeignKey('Dependencia', models.DO_NOTHING, db_column='iddependencia', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'habitacion'


class Menor(models.Model):
    idmenor = models.AutoField(db_column='idMenor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    idadulto = models.ForeignKey('Visitante', models.DO_NOTHING, db_column='idadulto')

    class Meta:
        managed = False
        db_table = 'menor'


class Operarios(models.Model):
    idlogin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    identificacion = models.IntegerField()
    privilegio = models.IntegerField()
    usuario = models.CharField(max_length=16)
    contrasena = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'operarios'


class Perfiloperario(models.Model):
    empresa = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    operario = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'perfiloperario'


class Permisos(models.Model):
    nombre = models.CharField(max_length=45)
    idpermiso = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permisos'


class Torre(models.Model):
    idtorre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    npisos = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'torre'



class Visitante(models.Model):
    idvisitante = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    idcama = models.PositiveIntegerField()
    iddependencia = models.ForeignKey('Dependencia', models.DO_NOTHING, db_column='iddependencia')
    nummenores = models.PositiveIntegerField(db_column='NumMenores', blank=True, null=True)  # Field name made lowercase.
    visitas = models.IntegerField(blank=True, null=True)
    nvisitas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visitante'

