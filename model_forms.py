from django import forms

from . import models as static_html_models

class StaticHtml(forms.ModelForm):

    class Meta:
        model = static_html_models.StaticHtml
        fields = (
            'url',
            'description',
        )

        widgets = {
            'url': forms.TextInput(),

            'description': forms.Textarea(attrs={
                'style': 'display: none;',

            }),
        }

        labels = {
            'description': '',
        }
