from django import forms
from django.forms import widgets
from webapp.models import Status, Type


class TackerForm(forms.Form):
    short_description = forms.CharField(max_length=100, required=True, label='Goal')
    content = forms.CharField(max_length=2000, required=False, label='Content', widget=widgets.Textarea)
    type = forms.ModelMultipleChoiceField(required=False, queryset=Type.objects.all(), widget=widgets.CheckboxSelectMultiple)
    status = forms.ModelChoiceField(queryset=Status.objects.all())
