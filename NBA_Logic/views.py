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
        ID = Tom.setup(nbaPlayerName)





        if (ID != "invalid"):
            reggames = Tom.RegularSeasonGamesPlayed(ID)
            playoffgames = Tom.PlayoffGamesPlayed(ID)

            if(playoffgames == 0):
                # If the player has played zero playoff games, so only has regular season games
                return render(request,"index.html")
                
        

            
            
            regularSeasonFG = Tom.RegularFG(ID)
            playoffsFG = Tom.PlayoffsFG(ID)

            regularSeason3pointFG = Tom.Regular3pointfg(ID)
            playoffs3pointFG = Tom.Playoffs3pointfg(ID)

            regularSeasonFreeThrow = Tom.RegularFreeThrow(ID)
            playoffsFreeThrow = Tom.PlayoffsFreeThrow(ID)


            

            data = {
            'regfg': regularSeasonFG,
            'playoffsfg': playoffsFG,
            'reg3fg' : regularSeason3pointFG,
            'playoffs3fg': playoffs3pointFG,
            'regfreethrow' : regularSeasonFreeThrow,
            'playoffsfreethrow' : playoffsFreeThrow,
            }
            return render(request, "results.html", {'name':nbaPlayerName, 'data':data, 'reggames':reggames, 'playoffgames':playoffgames})


         


        # return the data from the business logic and then display this on the SAME HTML page as the input bar,
        # but in a section below it. Also it will bring the user down to this section with a smooth animation

    return render(request, "results.html", {'name':"Invalid player"})


def goBack(request):
    
    return render(request,"index.html")