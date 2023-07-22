from django.shortcuts import render

def base(request):
    return render(request, 'myapp/base.html')

def home(request):
    return render(request, 'myapp/home.html')

def aboutus(request):
    return render(request, 'myapp/aboutus.html')

def advices(request):
    return render(request, 'myapp/advices.html')

def menu(request):
    return render(request, 'myapp/menu.html')

def services(request):
    return render(request, 'myapp/services.html')

def contact(request):
    return render(request, 'myapp/contact.html')
