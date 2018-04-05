from django import forms
from django_filters import Filter
import datetime

class DateRangeWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        attrs_from = {'class': 'date-from'}
        attrs_to = {'class': 'date-to'}

        if attrs:
            attrs_from.update(attrs)
            attrs_to.update(attrs)

        widgets = (forms.TextInput(attrs=attrs_from), forms.TextInput(attrs=attrs_to))
        super(DateRangeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]

    def format_output(self, rendered_widgets):
        return '<div class="date-range">' + ' - '.join(rendered_widgets) + '</div>'


class DateRangeField(forms.MultiValueField):
    widget = DateRangeWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.DateField(),
            forms.DateField(),
        )
        super(DateRangeField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return slice(*data_list)
        return None


class DateRangeFilter(Filter):
    field_class = DateRangeField

    def filter(self, qs, value):
        date_start = datetime.datetime.combine(value.start, datetime.time(0, 0, 0))
        date_stop = datetime.datetime.combine(value.stop, datetime.time(23, 59, 59))

        if value:
            lookup = '%s__range' % self.name
            return qs.filter(**{lookup: (date_start, date_stop)})
        return qs
