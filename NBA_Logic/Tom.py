#This file will contain the code for the display of the shot data in the regular season and in the playoffs
from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats.static import players, teams
import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguegamefinder, commonplayerinfo, commonallplayers
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playercareerstats


all_players_dict = 0 
nba_players_df = 0


def getAllPlayersList():
    global all_player_dict
    global nba_players_df
    all_players_dict = players.get_players()
    nba_players_df = pd.DataFrame(all_players_dict)
    firstLast_df = nba_players_df['full_name']
    firstLast_list = firstLast_df.tolist()
    return firstLast_list


def setup(name):
  
    playerName = name.title()
    global all_player_dict
    global nba_players_df
    all_players_dict = players.get_players()
    nba_players_df = pd.DataFrame(all_players_dict)


    if(playerName == "Lebron James"):
        playerName = "LeBron James"
    
    #boom, okay so now we have access to the given player in my algorithm 
    #now do some input validation
    
    

    #obtain the ID for this given player:

    everyPlayerIDandName = {}

    everyPlayerName = everyPlayerIDandName.values()

    #start of input validation-----------------------------------

    for player in all_players_dict:
        player_id = player['id']
        player_name = player['full_name']
        everyPlayerIDandName[player_id] = player_name



    if (playerName not in everyPlayerName):
       
        return "invalid"
    
    #Also need to check for capitalization stuff eg: Lebron James = LeBron James = lebron james

    

    #end of input validation---------------------------------------


    for player in all_players_dict:
        if player['full_name'] == playerName:
            playerDict  = player
        else:
            continue


    playerID = playerDict["id"]
   
    return (playerID)




careerStatsRegularDF= 0 
careerStatsPlayoffsDF= 0 


def getCareerStatsRegularSeason(playerID):
    global careerStatsRegularDF
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_regular_season
    careerStatsDF = regularSeasonTotalsDataSet.get_data_frame()
    if (careerStatsDF.empty):
        return 0
    careerStatsRegularDF = careerStatsDF
#Now the regularDFBron variable is assigned


def getCareerStatsPlayoffs(playerID):
    global careerStatsPlayoffsDF
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_post_season
    careerStatsDF = regularSeasonTotalsDataSet.get_data_frame()
    if (careerStatsDF.empty):
        return 0
    careerStatsPlayoffsDF = careerStatsDF
#Now the regularDFBron variable is assigned




def RegularSeasonGamesPlayed(playerID):
    getCareerStatsRegularSeason(playerID=playerID)
    regularFGBron = careerStatsRegularDF['GP']
    GPregular = regularFGBron.item()
    return GPregular




def PlayoffGamesPlayed(playerID):
    getCareerStatsPlayoffs(playerID=playerID)
    playoffsFGBron = careerStatsPlayoffsDF['GP']
     
    GPPlayoffs = playoffsFGBron.item()


    return GPPlayoffs



def RegularFG(playerID):
    getCareerStatsRegularSeason(playerID=playerID)
    regularFGBron = careerStatsRegularDF['FG_PCT']
    FGregularSeason = regularFGBron.item()
  
    return FGregularSeason


def PlayoffsFG(playerID):
    getCareerStatsPlayoffs(playerID=playerID)
    playoffsFGBron = careerStatsPlayoffsDF['FG_PCT']
    FGplayoffs = playoffsFGBron.item()
    
    return FGplayoffs




def Regular3pointfg(playerID):
    regularFGBron = careerStatsRegularDF['FG3_PCT']
    threeFGregularSeason = regularFGBron.item()

    return threeFGregularSeason



def Playoffs3pointfg(playerID):
    playoffsFGBron = careerStatsPlayoffsDF['FG3_PCT']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs







def RegularFreeThrow(playerID):
    regularFGBron = careerStatsRegularDF['FT_PCT']
    threeFGregularSeason = regularFGBron.item()
    

    return threeFGregularSeason



def PlayoffsFreeThrow(playerID):
    playoffsFGBron = careerStatsPlayoffsDF['FT_PCT']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs



def regularTotalPoints(playerID):
    playoffsFGBron =  careerStatsRegularDF['PTS']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs


def playoffsTotalPoints(playerID):
    playoffsFGBron = careerStatsPlayoffsDF['PTS']
    threeFGplayoffs = playoffsFGBron.item()


    return threeFGplayoffs




def regularTotalAssists(playerID):
    playoffsFGBron = careerStatsRegularDF['AST']
    threeFGplayoffs = playoffsFGBron.item()
 
    return threeFGplayoffs


def playoffsTotalAssists(playerID):
    playoffsFGBron = careerStatsPlayoffsDF['AST']
    threeFGplayoffs = playoffsFGBron.item()

    return threeFGplayoffs


def regularTotalRebounds(playerID):
    playoffsFGBron = careerStatsRegularDF['REB']
    threeFGplayoffs = playoffsFGBron.item()
  
    return threeFGplayoffs


def playoffsTotalRebounds(playerID):
    playoffsFGBron = careerStatsPlayoffsDF['REB']
    threeFGplayoffs = playoffsFGBron.item()
  

    return threeFGplayoffs


def regularTotalTurnovers(playerID):
    playoffsFGBron = careerStatsRegularDF['TOV']
    threeFGplayoffs = playoffsFGBron.item()
    print(threeFGplayoffs)
    
    return threeFGplayoffs


def playoffsTotalTurnovers(playerID):
    playoffsFGBron = careerStatsPlayoffsDF['TOV']
    threeFGplayoffs = playoffsFGBron.item()
   
    return threeFGplayoffs







def regularTotalBlocks(playerID):
    playoffsFGBron = careerStatsRegularDF['BLK']
    threeFGplayoffs = playoffsFGBron.item()
   
    return threeFGplayoffs


def playoffsTotalBlocks(playerID):
    playoffsFGBron = careerStatsPlayoffsDF['BLK']
    threeFGplayoffs = playoffsFGBron.item()

    return threeFGplayoffs



def regularTotalSteals(playerID):
    playoffsFGBron = careerStatsRegularDF['STL']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs


def playoffsTotalSteals(playerID):
    playoffsFGBron = careerStatsPlayoffsDF['STL']
    threeFGplayoffs = playoffsFGBron.item()
  

    return threeFGplayoffs



def regularTotalMinutes(playerID):
    playoffsFGBron = careerStatsRegularDF['MIN']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs


def playoffsTotalMinutes(playerID):
    playoffsFGBron = careerStatsPlayoffsDF['MIN']
    threeFGplayoffs = playoffsFGBron.item()

    return threeFGplayoffs
