#This file will contain the code for the display of the shot data in the regular season and in the playoffs
from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats.static import players, teams
import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguegamefinder, commonplayerinfo, commonallplayers
from nba_api.stats.library.parameters import SeasonAll

from nba_api.stats.endpoints import playercareerstats



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
        return "invalid"
    
    #Also need to check for capitalization stuff eg: Lebron James = LeBron James = lebron james

    

    #end of input validation---------------------------------------


    for player in all_players_dict:
        if player['full_name'] == playerName:
            playerDict  = player
        else:
            continue


    playerID = playerDict["id"]
    print(playerID)
    return (playerID)




def RegularSeasonGamesPlayed(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_regular_season
    regularDFBron = regularSeasonTotalsDataSet.get_data_frame()
    if (regularDFBron.empty):
        print("No regular season games played")
        return 0
    regularFGBron = regularDFBron['GP']
    GPregular = regularFGBron.item()
    return GPregular




def PlayoffGamesPlayed(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    if (playoffsDFBron.empty):
        print("No playoff games played")
        return 0
    playoffsFGBron = playoffsDFBron['GP']
     
    GPPlayoffs = playoffsFGBron.item()
    

    print(GPPlayoffs)


    return GPPlayoffs

 






def RegularFG(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_regular_season
    regularDFBron = regularSeasonTotalsDataSet.get_data_frame()
    regularFGBron = regularDFBron['FG_PCT']
    FGregularSeason = regularFGBron.item()
    print (FGregularSeason)
    return FGregularSeason





def PlayoffsFG(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['FG_PCT']
    FGplayoffs = playoffsFGBron.item()
    print (FGplayoffs)
    return FGplayoffs




def Regular3pointfg(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_regular_season
    regularDFBron = regularSeasonTotalsDataSet.get_data_frame()
    regularFGBron = regularDFBron['FG3_PCT']
    threeFGregularSeason = regularFGBron.item()
    print (threeFGregularSeason)

    return threeFGregularSeason



def Playoffs3pointfg(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['FG3_PCT']
    threeFGplayoffs = playoffsFGBron.item()
    print (threeFGplayoffs)
    return threeFGplayoffs







def RegularFreeThrow(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_regular_season
    regularDFBron = regularSeasonTotalsDataSet.get_data_frame()
    regularFGBron = regularDFBron['FT_PCT']
    threeFGregularSeason = regularFGBron.item()
    print (threeFGregularSeason)

    return threeFGregularSeason



def PlayoffsFreeThrow(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['FT_PCT']
    threeFGplayoffs = playoffsFGBron.item()
    print (threeFGplayoffs)
    return threeFGplayoffs












