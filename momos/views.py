from django.shortcuts import render, redirect
from . models import momomessage

from django.contrib.auth.models import User

import datetime

# Create your views here.


def home(request):
    return render(request, 'momos/home.html')


def footer(request):
    return render(request,  'momos/footer.html')


def contact(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        reason = request.POST['reason']
        email = request.POST['email']
        phonenumber = request.POST['phone']
        message = request.POST['message']

        print(firstname, lastname, reason, email, phonenumber, message)

        momomessage.objects.create()

    return render(request, 'momos/contact1.html')


def contact1(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        select = request.POST['select']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        msg = request.POST['msg']

        user = User.objects.first()

        momomessage.objects.create(
            firstname=firstname, lastname=lastname, select=select, email=email, phonenumber=phonenumber, msg=msg, created_by=user, created_at=datetime.datetime.now())

    return render(request, 'momos/contact1.html')
