from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random
import string

def home(request):
    return render(request,'r_p_g/index.html')

def password(request):
    length = int(request.GET.get('Length',8))
    pass1  = list(string.ascii_lowercase)

    if request.GET.get('Uppercase'):
        pass1.extend(list(string.ascii_uppercase))
        
    if request.GET.get('Special Symbol'):
        pass1.extend(list(string.punctuation))
    
    if request.GET.get('Numbers'):
        pass1.extend(list(string.digits))
    
    thepass = ''

    for i in range(length):
        thepass += random.choice(pass1)
    
    return render(request,'r_p_g/result.html',{'password':thepass})
