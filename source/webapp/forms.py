from django import forms
from django.forms import widgets, ValidationError
from webapp.models import Tracker


class TackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['short_description', 'content', 'type', 'status']
        widgets = {'type': widgets.CheckboxSelectMultiple}

    def clean_short_description(self):
        short_description = self.cleaned_data['short_description']
        if len(short_description) < 5:
            self.add_error('short_description', ValidationError('This field should be at least %(length)d symbols long!'
                                                                , code='too_short', params={'length': 5}))
        if len(short_description) > 20:
            self.add_error('short_description', ValidationError('This field should be at least %(length)d symbols long!'
                                                                , code='too_long', params={'length': 20}))
        return short_description

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['short_description'] == cleaned_data['content']:
            raise ValidationError("Text of the article should not duplicate it's title!")
        if len(cleaned_data['content']) < 75:
            self.add_error('short_description', ValidationError('This field should be at least %(length)d symbols long!'
                                                                , code='too_short', params={'length': 75}))
        if len(cleaned_data['content']) > 200:
            self.add_error('short_description', ValidationError('This field should be at least %(length)d symbols long!'
                                                                , code='too_long', params={'length': 200}))
        return cleaned_data







