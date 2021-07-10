from django import forms
from django.utils import html


class SubmitButtonWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return f'<input type="submit" name="{html.escape(name)}" value="{html.escape(value)}">'


class SubmitButtonField(forms.Field):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = {}
        kwargs["widget"] = SubmitButtonWidget

        super(SubmitButtonField, self).__init__(*args, **kwargs)

    def clean(self, value):
        return value