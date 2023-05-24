from django.shortcuts import render
from django.http import HttpResponse
import Mahmoud

# Create your views here.



def home(request):
    number = Mahmoud.random()
    context = {'random_number': number}
    
    return render(request, 'index.html', context)