from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    charecters = list('abcdefghijklmnopqrstuvwxyz')
    
    length = int(request.GET.get('length',12))
    
    if request.GET.get('uppercase'):
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('uppercase'):
        charecters.extend(list('!@#$%^&*()'))
        
    if request.GET.get('number'):
        charecters.extend(list('0123456789'))
        
    the_password = ''
    
    for x in range(length):
        
        the_password += random.choice(charecters)
        
    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'generator/about.html')