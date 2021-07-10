from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm
# Create your views here.


def register_view(request):
    registration = RegistrationForm()
    if request.method == 'POST':
        registration = RegistrationForm(request.POST)
        if registration.is_valid():
            if registration.cleaned_data['Password'] != registration.cleaned_data['Confirm_Password']:
                registration.add_error('Confirm_Password', 'Passwords Did not match. Please Try Again!')
            else:
                user = User.objects.create_user(username=registration.cleaned_data['UserName'],
                                                email=registration.cleaned_data['Email'],
                                                password=registration.cleaned_data['Password'])
                user.save()
                registration.save()
                messages.add_message(request, messages.SUCCESS, 'Account Created Successfully!')
                return redirect(request.META['HTTP_REFERER'])
    return render(request, 'RegisterAccount/index.html', {'registerForm': registration})