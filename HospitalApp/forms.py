from django import forms
from HospitalApp.models import Dependencia
from HospitalApp.models import Torre
from HospitalApp.models import Habitacion
from HospitalApp.models import Cama
from django.contrib.auth.models import User
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class Dependecias(forms.ModelForm):
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
    menores = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'placeholder': 'Escriba el numero de menores que puede acompañarm a cada adulto dependencia...',
        'min': '0',
        'class': 'form-control',
        }

    ))
    class Meta:
        model = Dependencia
        fields = ('nombres','hora_inicio','hora_fin','cupo','menores')


class Torres(forms.ModelForm):
    nombre =  forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el nombre de la torre...'
        }
    ))
    npisos = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el numero de pisos de la torre...'
        }
    ))
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

class Habitaciones(forms.ModelForm):
    nombrehabitacion = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el nombre de la habitacion...'
        }
    ))

    piso = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el piso en el cual está ubicada la habitacion...'
        }
    ))

    idtorre = nombreChoiceField(queryset=Torre.objects.all())

    ncamas = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el numero de camas...'
        }
    ))

    class Meta:
        model = Habitacion
        fields = ('nombrehabitacion', 'piso', 'idtorre','ncamas')



class Camas(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el nombre de la cama...'
        }
    ))
    idhabitacion = habitacionChoiceField(queryset=Habitacion.objects.all())
    iddependencia = dependeciaChoiceField(queryset=Dependencia.objects.all())
    disponibilidad = Dependencia.objects.all()
    class Meta:
        model = Cama
        fields = ('nombre', 'idhabitacion', 'iddependencia', )


class ConsultaCamas(forms.ModelForm):
    nombre = camaChoiceField(queryset=Cama.objects.filter(ocupacion__gt=0))
    class Meta:
        model = Cama
        fields = ('nombre','idcama')


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

class CustomUserCreationForm(forms.Form):
    permisos = (('operario', 'Operario'),
                ('administrativo','Administrativo'))
    username = forms.CharField(label='Nombre de usuario', min_length=4, max_length=150)
    first_name = forms.CharField(label = 'Nombre', max_length=25)
    last_name = forms.CharField(label='Apellido', max_length=25)
    permiso = forms.ChoiceField(choices=permisos,label='Permiso',)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    passconsola = forms.CharField(label='Contraseña consola', max_length=25)

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
        user.passconsola = self.cleaned_data['passconsola']
        user.save()
        return user
