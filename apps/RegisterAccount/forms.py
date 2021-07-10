#from django.contrib.auth.forms import UserCreationForm
#from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User
from django import forms
from .models import RegisterDetails
from apps.ButtonField import SubmitButtonField


class RegistrationForm(forms.ModelForm):

    Confirm_Password = forms.CharField(widget=forms.TextInput())
    submitButton = SubmitButtonField(label="", initial="Submit")

    class Meta:
        model = RegisterDetails
        fields = '__all__'
        labels = {'Mob_No': 'Mobile Number', 'Aadhar_No': 'Aadhaar Number', 'Pan_No': 'Pan Card Number'}
        widgets = {
                    'Email': forms.EmailInput(),
                    'Password': forms.PasswordInput(attrs={'data-toggle': 'password'}),
                    'User_Type': forms.RadioSelect(choices=([('User', 'Normal'), ('Staff', 'Staff')])),
                    'Current_Address': forms.Textarea(attrs={'maxlength': 50, 'rows': 2}),
                    'Permanent_Address': forms.Textarea(attrs={'maxlength': 50, 'rows': 2}),
                    'Mob_No': forms.TextInput(attrs={'min': 6260000000, 'max': 9999999999, 'type': 'number'})
        }


# class CustomUserCreationForm(forms.Form):
#     username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
#     email = forms.EmailField(label='Enter email')
#     password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
#
#     def clean_username(self):
#         username = self.cleaned_data['username'].lower()
#         r = User.objects.filter(username=username)
#         if r.count():
#             raise  ValidationError("Username already exists")
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         r = User.objects.filter(email=email)
#         if r.count():
#             raise  ValidationError("Email already exists")
#         return email
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Password don't match")
#
#         return password2
#
#     def save(self, commit=True):
#         user = User.objects.create_user(
#             self.cleaned_data['username'],
#             self.cleaned_data['email'],
#             self.cleaned_data['password1']
#         )
#         return user