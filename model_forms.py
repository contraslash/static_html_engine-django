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

class StaticHtmlMarkdown(forms.ModelForm):

    class Meta:
        model = static_html_models.StaticHtml
        fields = (
            'url',
            'description',
            'markdown'
        )

        widgets = {
            'url': forms.TextInput(),

            'markdown': forms.Textarea(attrs={
                'class': 'materialize-textarea wmd-input-markdown',
                'id': 'wmd-input-markdown'
            }),

            'description': forms.Textarea(attrs={
                'style': 'display: none;',

            }),
        }

        labels = {
            'description': '',
        }
