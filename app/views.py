from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    send_mail('Hey send from ibrahim Ogundipe',
    'Hi, This mail is from Ibrahim Ogundipe',
    'ogundipeibrahim19@gmail.com',
    ['ogundipeibrahim1111@gmail.com',],
    fail_silently=False)
    return render(request, 'home.html')