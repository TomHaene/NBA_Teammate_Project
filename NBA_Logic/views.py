from django.shortcuts import render
from django.http import HttpResponse
import NBA_Logic.thomas as Thomas


# Create your views here.


def index(request):
    allplayers = Thomas.getAllPlayersList()

    return render(request,"index.html",{ "allplayers": allplayers})




def returnResults(request):
   
    if request.method == "POST":
        nbaPlayerName = request.POST.get("PlayerName")
        
        request.session['name'] = nbaPlayerName

        # now need to pass this name to the Tom.py file
        ID = Thomas.setup(nbaPlayerName)

    


        if (ID != "invalid"):
            reggames = Thomas.RegularSeasonGamesPlayed(ID)
            playoffgames = Thomas.PlayoffGamesPlayed(ID)

            if(playoffgames == 0):
                # If the player has played zero playoff games, so only has regular season games
                return render(request,"index.html")
                
        
            regularSeasonFG = Thomas.RegularFG(ID)
            playoffsFG = Thomas.PlayoffsFG(ID)

            regularSeason3pointFG = Thomas.Regular3PointFG(ID)
            playoffs3pointFG = Thomas.Playoffs3PointFG(ID)

            regularSeasonFreeThrow = Thomas.RegularFreeThrow(ID)
            playoffsFreeThrow = Thomas.PlayoffsFreeThrow(ID)

            regularTotalPoints = Thomas.RegularTotalPoints(ID)
            playoffTotalPoints = Thomas.PlayoffsTotalPoints(ID)

            regularTotalAssists = Thomas.RegularAssists(ID)
            playoffTotalAssists = Thomas.PlayoffsAssists(ID)

            regularTotalRebounds = Thomas.RegularRebounds(ID)
            playoffTotalRebounds = Thomas.PlayoffsRebounds(ID)

            regularTotalTurnovers = Thomas.RegularTurnovers(ID)
            playoffTotalTurnovers = Thomas.PlayoffsTurnovers(ID)

            regularTotalBlocks = Thomas.RegularBlocks(ID)
            playoffTotalBlocks = Thomas.PlayoffsBlocks(ID)

            regularTotalSteals = Thomas.RegularSteals(ID)
            playoffTotalSteals = Thomas.PlayoffsSteals(ID)

            regularTotalMinutes = Thomas.RegularMinutes(ID)
            playoffTotalMinutes = Thomas.PlayoffsMinutes(ID)




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
        allplayers = Thomas.getAllPlayersList()

        return render(request,"index.html", {'allplayers': allplayers})



        # return the data from the business logic and then display this on the SAME HTML page as the input bar,
        # but in a section below it. Also it will bring the user down to this section with a smooth animation

    return render(request, "results.html", {'name':"Invalid player"})


def goBack(request):
    allplayers = Thomas.getAllPlayersList()

    return render(request,"index.html",{ "allplayers": allplayers})




