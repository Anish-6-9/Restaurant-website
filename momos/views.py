from django.shortcuts import render, redirect

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

    return render(request, 'momos/contact.html')
