#This file will contain the code for the display of the shot data in the regular season and in the playoffs
from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats.static import players, teams
import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguegamefinder, commonplayerinfo, commonallplayers
from nba_api.stats.library.parameters import SeasonAll



def setup(name):
    playerName = name
    #boom, okay so now we have access to the given player in my algorithm 
    #now do some input validation
    all_players_dict = players.get_players()
    nba_players_df = pd.DataFrame(all_players_dict)

    #obtain the ID for this given player:

    everyPlayerIDandName = {}
    everyPlayerName = everyPlayerIDandName.values()




    #start of input validation-----------------------------------

    for player in all_players_dict:
        player_id = player['id']
        player_name = player['full_name']
        everyPlayerIDandName[player_id] = player_name


    if (playerName not in everyPlayerName):
        print("Invalid player")
        return
    
    #Also need to check for capitalization stuff eg: Lebron James = LeBron James = lebron james


    #end of input validation---------------------------------------


    for player in all_players_dict:
        if player['full_name'] == playerName:
            playerDict  =player
        else:
            continue
    

    player_id = playerDict["id"]
    print(player_id)






















