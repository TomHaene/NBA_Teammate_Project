from django.shortcuts import render
from django.http import HttpResponse
import NBA_Logic.Tom as Tom


# Create your views here.


def index(request):
    #allplayers = Tom.getAllPlayersList()

    return render(request,"index.html")




def returnResults(request):
   
    if request.method == "POST":
        nbaPlayerName = request.POST.get("PlayerName")
        
        request.session['name'] = nbaPlayerName

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

            regularTotalPoints = Tom.regularTotalPoints(ID)
            playoffTotalPoints = Tom.playoffsTotalPoints(ID)

            regularTotalAssists = Tom.regularTotalAssists(ID)
            playoffTotalAssists = Tom.playoffsTotalAssists(ID)

            regularTotalRebounds = Tom.regularTotalRebounds(ID)
            playoffTotalRebounds = Tom.playoffsTotalRebounds(ID)

            regularTotalTurnovers = Tom.regularTotalTurnovers(ID)
            playoffTotalTurnovers = Tom.playoffsTotalTurnovers(ID)

            regularTotalBlocks = Tom.regularTotalBlocks(ID)
            playoffTotalBlocks = Tom.playoffsTotalBlocks(ID)

            regularTotalSteals = Tom.regularTotalSteals(ID)
            playoffTotalSteals = Tom.playoffsTotalSteals(ID)

            regularTotalMinutes = Tom.regularTotalMinutes(ID)
            playoffTotalMinutes = Tom.playoffsTotalMinutes(ID)




            if(reggames != 0 and playoffgames !=0):
                regularPPG = regularTotalPoints / reggames
                playoffsPPG = playoffTotalPoints / playoffgames

                regularAPG = regularTotalAssists / reggames
                playoffsAPG = playoffTotalAssists / playoffgames

                regularRPG = regularTotalRebounds / reggames
                playoffsRPG = playoffTotalRebounds / playoffgames

                regularTPG = regularTotalTurnovers / reggames
                playoffsTPG = playoffTotalTurnovers / playoffgames

                regularBPG = regularTotalBlocks / reggames
                playoffsBPG = playoffTotalBlocks / playoffgames

                regularSPG = regularTotalSteals / reggames
                playoffsSPG = playoffTotalSteals/ playoffgames

                regularMPG = regularTotalMinutes / reggames
                playoffsMPG = playoffTotalMinutes / playoffgames


        
            
            #These are both lists of tuples we must now pass these to the heap maps

        
            data = {
            'regfg': regularSeasonFG,
            'playoffsfg': playoffsFG,
            'reg3fg' : regularSeason3pointFG,
            'playoffs3fg': playoffs3pointFG,
            'regfreethrow' : regularSeasonFreeThrow,
            'playoffsfreethrow' : playoffsFreeThrow,
            'regppg': regularPPG,
            'playoffsppg':playoffsPPG,
            'regapg' : regularAPG,
            'playoffsapg': playoffsAPG,
            'regrpg' : regularRPG,
            'playoffsrpg': playoffsRPG,
            'regtpg' : regularTPG,
            'playoffstpg' : playoffsTPG,
            'regbpg' : regularBPG,
            'playoffsbpg': playoffsBPG,
            'regspg' : regularSPG,
            'playoffsspg' : playoffsSPG,
            'regmpg' : regularMPG,
            'playoffsmpg': playoffsMPG

            }
            return render(request, "results.html", {'name':nbaPlayerName, 'data':data, 'reggames':reggames, 'playoffgames':playoffgames})

        #Now handle if the name is not a valid nba player eg: Tom Haene
        allplayers = Tom.getAllPlayersList()

        return render(request,"index.html", {'allplayers': allplayers})



        # return the data from the business logic and then display this on the SAME HTML page as the input bar,
        # but in a section below it. Also it will bring the user down to this section with a smooth animation

    return render(request, "results.html", {'name':"Invalid player"})


def goBack(request):
    #allplayers = Tom.getAllPlayersList()

    return render(request,"index.html")





def testing(request):
     if request.method == "POST":
        nbaPlayerName = request.POST.get("PlayerName")
        
        request.session['name'] = nbaPlayerName

        # now need to pass this name to the Tom.py file
        ID = Tom.setup(nbaPlayerName)
    
     
        if (ID != "invalid"):
            reggames = Tom.RegularSeasonGamesPlayed(ID)
            playoffgames = Tom.PlayoffGamesPlayed(ID)
            return render(request,"results.html" ,{'name':nbaPlayerName, 'reggames': reggames, 'playoffgames': playoffgames})


    