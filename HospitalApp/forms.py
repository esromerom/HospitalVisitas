from django import forms
from HospitalApp.models import Dependencia
from HospitalApp.models import Torre
from HospitalApp.models import Habitacion
from HospitalApp.models import Cama
from django.contrib.auth.models import User
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class Torres(forms.ModelForm):
    nombre =  forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el nombre de la torre...'
        }
    ),label='Nombre de Torre')
    npisos = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el numero de pisos de la torre...'
        }
    ),label='Numero de Pisos')
    class Meta:
        model = Torre
        fields = ('nombre', 'npisos')


class nombreChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.nombre)


class habitacionChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.nombrehabitacion)


class camaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.nombre)


class dependeciaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.nombres)


class torreChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.nombre)


class CrearDependecias(forms.ModelForm):
    nombres = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Escriba el nombre de la dependencia...'
                                }
                            ))
    hora_inicio = forms.TimeField(widget=forms.TimeInput(
                                        attrs={
                                            'placeholder': 'Escriba la hora de inicio de visitas...',
                                             'class': 'form-control',
                                        }
                                    ))
    hora_fin = forms.TimeField(widget=forms.TimeInput(
                                    attrs={
                                        'placeholder': 'Escriba la hora de inicio de visitas..,',
                                         'class': 'form-control',
                                    }
                                ))
    cupo = forms.IntegerField(widget=forms.NumberInput(
                                attrs={
                                    'placeholder': 'Escriba el numero de visitantes que pueden ingresar por cama...',
                                    'min': '0',
                                    'class': 'form-control',
                                }
                            ))
    # menores = forms.IntegerField(widget=forms.NumberInput(
    #                                 attrs={
    #                                     'placeholder': 'Escriba el numero de menores que puede acompañarma cada adulto dependencia...',
    #                                 'min': '0',
    #                                 'class': 'form-control',
    #                                 }
    #                             ))

    # def clean_nombres(self):
    #     nombres = self.cleaned_data['nombres'].lower()
    #     r = User.objects.filter(nombres=nombres)
    #     if r.count():
    #         raise ValidationError("Esta dependencia ya existe.")
    #     return nombres

    class Meta:
        model = Dependencia
        fields = ('nombres',
                  'hora_inicio',
                  'hora_fin',
                  'cupo',
                  # 'menores',
                  )


class EditarDependencias(forms.Form):
    iddependencia = dependeciaChoiceField(queryset=Dependencia.objects.all(), label='Área')
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Escriba el nuevo de la dependencia...'
                                                            }))

    class Meta:
        model = Dependencia
        fields = ('iddependencia',
                  'nombres',)
        sequence = ('iddependencia',
                  'nombres',)

    def clean_nombres(self):  # Revision no exista esa habitacion
        nombres = self.cleaned_data['nombres']

        try:
            dep = Dependencia.objects.get(nombres__iexact=nombres)

        except:
            return nombres
        raise forms.ValidationError(("Esa área ya existe."))


class ConsultaDependencias(forms.Form):
    iddependencia = dependeciaChoiceField(queryset=Dependencia.objects.all(), label='Área a editar')
    class Meta:
        model = Dependencia
        fields = ('iddependencia',)


class CrearHabitaciones(forms.ModelForm):
    nombrehabitacion = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Escriba el nombre de la habitacion...'
                                }
                        ),label='Nombre de habitación')
    piso = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Escriba el piso en el cual está ubicada la habitacion...'
                                }
                            ),label= 'Piso')

    idtorre = nombreChoiceField(queryset=Torre.objects.all(),label='Torre')
    iddependencia = dependeciaChoiceField(queryset=Dependencia.objects.all(),label='Área')
    ncamas = forms.IntegerField(widget=forms.NumberInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Escriba el numero de camas...'
                                    }
                                ),label='Número de camas')

    class Meta:
        model = Habitacion
        fields = ('nombrehabitacion', 'piso', 'idtorre','iddependencia','ncamas',)

    def clean_nombrehabitacion(self): #Revision no exista esa habitacion
        nombrehabitacion = self.cleaned_data['nombrehabitacion']

        try:
            hab = Habitacion.objects.get(nombrehabitacion__iexact=nombrehabitacion)

        except:
            return nombrehabitacion
        raise forms.ValidationError(("Ese nombre de cama ya existe."))


class EditarHabitaciones(forms.Form):
    idhabitacion = habitacionChoiceField(queryset=Habitacion.objects.all(), label='Habitación a editar')
    nombrehabitacion = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Escriba el nombre de la habitacion...'
                                }
                        ),label='Nuevo Nombre de habitación')
    piso = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Escriba el piso en el cual está ubicada la habitacion...'
                                }
                            ),label= 'Piso')

    idtorre = nombreChoiceField(queryset=Torre.objects.all(),label='Torre')
    iddependencia = dependeciaChoiceField(queryset=Dependencia.objects.all(),label='Área')
    ncamas = forms.IntegerField(widget=forms.NumberInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Escriba el numero de camas...'
                                    }
                                ),label='Número de camas')

    class Meta:
        model = Habitacion
        fields = ('idhabitacion','nombrehabitacion', 'piso', 'idtorre','ncamas','iddependencia',    )
        sequence = ('idhabitacion','nombrehabitacion', 'piso', 'idtorre','iddependencia','ncamas',)

    def clean_nombrehabitacion(self): #Revision no exista esa habitacion
        nombrehabitacion = self.cleaned_data['nombrehabitacion']
        idhabitacion = self.cleaned_data['idhabitacion']
        print (idhabitacion.nombrehabitacion)
        try:
            hab = Habitacion.objects.get(nombrehabitacion__iexact=nombrehabitacion)
            if nombrehabitacion != idhabitacion.nombrehabitacion:
                return nombrehabitacion
            raise forms.ValidationError(("Esa habitación ya existe."))
        except:
            return nombrehabitacion


class ConsultaHabitacion(forms.Form):
    idhabitacion = habitacionChoiceField(queryset=Habitacion.objects.all().order_by('nombrehabitacion'),
                                         label='Habitación a editar')
    class Meta:
        model = Habitacion
        fields = ('idhabitacion',)


class CrearCamas(forms.Form):
    idhabitacion = habitacionChoiceField(queryset=Habitacion.objects.all().order_by('nombrehabitacion'),
                                         label='Habitación')
    nombre = forms.CharField(widget=forms.TextInput(
                            attrs={'class': 'form-control',
                                   'placeholder': 'Escriba el nombre de la cama...'}))
    disponibilidad = forms.IntegerField(widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Escriba el cupo máximo aquí ...'}),label="Cupo")
    # iddependencia = dependeciaChoiceField(queryset=Dependencia.objects.all().order_by('nombres'),
    #                                      label='Dependencia', initial=8)

    class Meta:
        model = Cama
        fields = ('idhabitacion', 'disponibilidad', 'nombre',)
        sequence = ('idhabitacion', 'nombre', 'disponibilidad',)

    def clean_nombre(self): #Revision no exista esa habitacion
        nombre = self.cleaned_data['nombre']

        try:
            hab = Cama.objects.get(nombre__iexact=nombre)
        except:
            nomHab = self.cleaned_data['idhabitacion'].nombrehabitacion
            return nombre
        raise forms.ValidationError(("Ese nombre de cama ya existe."))


class EditarCamas(forms.Form):
    idcama = camaChoiceField(queryset=Cama.objects.all().order_by('nombre'),
                             label='Cama a editar')
    nombre = forms.CharField(widget=forms.TextInput(
                            attrs={'class': 'form-control',
                                   'placeholder': 'Escriba el nuevo nombre o reescriba el actual ...'}),label= "Nuevo Nombre")

    # idhabitacionnueva = habitacionChoiceField(queryset=Habitacion.objects.all().order_by('nombrehabitacion'),
    #                                      label='Habitación')
    disponibilidad = forms.IntegerField(widget=forms.NumberInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Escriba el cupo máximo aquí ...'}),label="Cupo")
    # ocupacion = forms.IntegerField(widget=forms.NumberInput(
    #     attrs={'class': 'form-control',
    #            'placeholder': 'Escriba el cupo máximo aquí ...'}), label="Ocupación")

    # iddependencia = dependeciaChoiceField(queryset=Dependencia.objects.all().order_by('nombres'),
    #                                      label='Dependencia', initial=8)

    class Meta:
        model = Cama
        fields = ('idcama', 'nombre',  'disponibilidad',)
        sequence = ['idcama', 'nombre', 'disponibilidad',]

    def clean_nombre(self): #Revision no exista esa habitacion
        nombre = self.cleaned_data['nombre']
        idcama = self.cleaned_data['idcama']
        try:
            hab = Cama.objects.get(nombre__iexact=nombre)
            if nombre != idcama.nombre:
                return nombre
            raise forms.ValidationError(("Ese nombre de cama ya existe."))
        except:
            return nombre



class ConsultaCamas(forms.Form):
    nombre = camaChoiceField(queryset=Cama.objects.filter(ocupacion__gt=0))
    class Meta:
        model = Cama
        fields = ('nombre',)


class FormReporteOcupacion(forms.ModelForm):
    comDependencia = dependeciaChoiceField(queryset=Dependencia.objects.all())
    class Meta:
        model = Dependencia
        fields = ('nombres',)


class OperarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = {
                    'username',
                    'first_name',
                    'last_name',
                  }

    def save(self, commit=True):
        user = super(OperarioForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class CreacionUsuario(forms.Form):
    permisos = (('operario', 'Operario'),
                ('administrativo','Administrativo'))
    username = forms.CharField(label='Nombre de usuario', min_length=4, max_length=150)
    first_name = forms.CharField(label = 'Nombre', max_length=25)
    last_name = forms.CharField(label='Apellido', max_length=25)
    permiso = forms.ChoiceField(choices=permisos,label='Permiso',)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("El nombre de usuario ya existe")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Esta cuenta de email ya está registrada")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data['username'],
                                        self.cleaned_data['email'],
                                        self.cleaned_data['password1'],
                                        is_staff = True if self.cleaned_data['permiso'] == 'administrativo' else False
                                        )
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
