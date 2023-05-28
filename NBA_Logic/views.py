from django.shortcuts import render
from django.http import HttpResponse
import Tom

# Create your views here.


def home(request):
    if request.method == 'POST':
        nbaPlayerName = request.POST.get("PlayerName")
        print(nbaPlayerName)
        #now need to pass this name to the Tom.py file
        Tom.main(nbaPlayerName)

        
        
    return render(request, "index.html")
