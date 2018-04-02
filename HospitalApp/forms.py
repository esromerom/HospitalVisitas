from django import forms
from HospitalApp.models import Dependencia
from HospitalApp.models import Torre
from HospitalApp.models import Habitacion
from HospitalApp.models import Cama

class HomeForm(forms.ModelForm):
    nombres = forms.CharField()
    hora_inicio = forms.TimeField()
    hora_fin = forms.TimeField()
    menores = forms.IntegerField()
    class Meta:

        model = Dependencia
        fields = ('nombres','hora_inicio','hora_fin','cupo','menores')


class Torres(forms.ModelForm):
    nombre =  forms.CharField()
    class Meta:
        model = Torre
        fields = ('nombre', 'npisos')


class nombreChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.nombre)


class habitacionChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.nombrehabitacion)


class dependeciaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.nombres)

class torreChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.nombre)

class Habitaciones(forms.ModelForm):
    nombrehabitacion = forms.CharField()
    piso = forms.CharField()
    idtorre = nombreChoiceField(queryset=Torre.objects.all())
    class Meta:
        model = Habitacion
        fields = ('nombrehabitacion', 'piso', 'idtorre','ncamas')


class Camas(forms.ModelForm):
    nombre = forms.CharField()
    idhabitacion = habitacionChoiceField(queryset=Habitacion.objects.all())
    iddependencia = dependeciaChoiceField(queryset=Dependencia.objects.all())
    disponibilidad = Dependencia.objects.all()
    class Meta:
        model = Cama
        fields = ('nombre', 'idhabitacion', 'iddependencia', )


class FormReporteOcupacion(forms.ModelForm):
    comDependencia = dependeciaChoiceField(queryset=Dependencia.objects.all())
    class Meta:
        model = Dependencia
        fields = ('nombres',)
