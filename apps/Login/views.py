from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
# Create your views here.


def login_view(request):
    loginData = LoginForm()
    try:
        if request.session['username'] is not None:
            return redirect('/account/')
    except:
        pass
    if request.method == 'POST':
        loginData = LoginForm(request.POST)
        if loginData.is_valid():
            username = loginData.cleaned_data['username']
            password = loginData.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("user authenticated")
                login(request, user)
                request.session['username'] = loginData.cleaned_data['username']
                return redirect('/account/')
            else:
                messages.add_message(request, messages.ERROR,
                                     "Username/Password did not match. Please try again!")
    return render(request, 'Login/index.html', {'loginData': loginData})
