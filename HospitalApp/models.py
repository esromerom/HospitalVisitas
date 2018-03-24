"""A model is the single, definitive source of information
about your data. It contains the essential fields and behaviors
of the data you’re storing. Generally, each model maps to a single
database table.

The basics:

- Each model is a Python class that subclasses django.db.models.Model.
- Each attribute of the model represents a database field.
- With all of this, Django gives you an automatically-generated
database-access API; see Making queries."""

from django.db import models
from django.contrib.auth.models import User
# Esa clas User es la que conecta a la tabla de auth_user


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
    idcama = models.PositiveIntegerField(blank=True, null=True)

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


class Dependencia(models.Model):
    iddependencia = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=45)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    cupo = models.PositiveIntegerField(blank=True, null=True)
    menores = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dependencia'


class Cama(models.Model):
    idcama = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre Cama',max_length=45)
    idhabitacion = models.ForeignKey('Habitacion', models.DO_NOTHING, db_column='idhabitacion')
    iddependencia = models.ForeignKey('Dependencia', models.DO_NOTHING, db_column='iddependencia')
    ocupacion = models.PositiveIntegerField(verbose_name='Ocupación')
    disponibilidad = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cama'


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


class Habitacion(models.Model):
    idhabitacion = models.AutoField(primary_key=True)
    nombrehabitacion = models.CharField(max_length=45)
    piso = models.CharField(max_length=45)
    idtorre = models.ForeignKey('Torre', models.DO_NOTHING, db_column='idtorre')
    ncamas = models.PositiveIntegerField()

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


class Torre(models.Model):
    idtorre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    npisos = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'torre'


class Visitante(models.Model):
    idvisitante = models.IntegerField(primary_key=True)
    nombre = models.CharField(verbose_name='Visitante',max_length=45)
    idcama = models.ForeignKey(Cama, models.DO_NOTHING, db_column='idcama')
    iddependencia = models.ForeignKey(Dependencia, models.DO_NOTHING, db_column='iddependencia')
    nummenores = models.PositiveIntegerField(db_column='NumMenores', blank=True, null=True)  # Field name made lowercase.
    foto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visitante'



