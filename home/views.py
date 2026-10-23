from django.shortcuts import render

def landing(request):
    return render(request, 'home/landing.html')

def home(request):
    context = {
        'title': 'Student Registration System',
        'message': 'Welcome to our Django application!',
        'show_message':True,
        'show_title':False
    }
    return render(request, 'home/home.html', context)