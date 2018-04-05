from django import forms
from HospitalApp.models import Dependencia
from HospitalApp.models import Torre
from HospitalApp.models import Habitacion
from HospitalApp.models import Cama

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
    nombre = camaChoiceField(queryset=Cama.objects.all())
    class Meta:
        model = Cama
        fields = ('nombre','idcama')


class ReporteOcupacion(forms.ModelForm):
    comDependencia = dependeciaChoiceField(queryset=Dependencia.objects.all())
    class Meta:
        model = Dependencia
        fields = ('nombres',)
