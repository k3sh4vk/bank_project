from django import forms
from .models import LoginModel
from apps.ButtonField import SubmitButtonField

class LoginForm(forms.ModelForm):

    submit = SubmitButtonField(label="", initial="Submit")

    class Meta:
        model = LoginModel
        fields = "__all__"
