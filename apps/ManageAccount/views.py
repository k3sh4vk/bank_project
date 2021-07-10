from django.shortcuts import render
from django.contrib.auth import authenticate, login
from apps.RegisterAccount.models import RegisterDetails as accountDetails
# Create your views here.


def account_view(request):
    accountData = accountDetails.objects.all()
    return render(request, 'ManageAccount/index.html', {'accountData': accountData})
