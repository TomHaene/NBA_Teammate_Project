from django.shortcuts import render
from django.http import HttpResponse
import Tom

# Create your views here.


def index(request):
    


    return render(request,"index.html")


def returnResults(request):
    if request.method == "POST":
        nbaPlayerName = request.POST.get("PlayerName")
        print(nbaPlayerName)
        # now need to pass this name to the Tom.py file
        Tom.setup(nbaPlayerName)
    
        # return the data from the business logic and then display this on the SAME HTML page as the input bar,
        # but in a section below it. Also it will bring the user down to this section with a smooth animation

    return render(request, "results.html", {'name':'Marcus Smart'})
