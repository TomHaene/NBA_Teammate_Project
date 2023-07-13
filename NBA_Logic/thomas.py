import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import time
import numpy as np
from nba_api.stats.static import players



all_players_dict = 0 
nba_players_df = 0


def getAllPlayersList():
    global all_players_dict
    global nba_players_df
    all_players_dict = players.get_players()
    nba_players_df = pd.DataFrame(all_players_dict)
    firstLast_df = nba_players_df['full_name']
    firstLast_list = firstLast_df.tolist()
    return firstLast_list


def setup(name):
  
    playerName = name.title()
    global all_players_dict
    global nba_players_df
    all_players_dict = players.get_players()
    nba_players_df = pd.DataFrame(all_players_dict)


    if(playerName == "Lebron James"):
        playerName = "LeBron James"

    if(playerName == "Tracy Mcgrady"):
        playerName == "Tracy McGrady"   

    if(playerName == "Demar Derozan"):
        playerName == "DeMar DeRozan"  

    if(playerName == "Demarcus Cousins"):
        playerName == "DeMarcus Cousins"    


    
    
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
    print(playerID)
   
    return (playerID)




regular_season_url = 'https://stats.nba.com/stats/leagueLeaders?ActiveFlag=No&LeagueID=00&PerMode=Totals&Scope=S&Season=All%20Time&SeasonType=Regular%20Season&StatCategory=PTS'
r = requests.get(url=regular_season_url).json()
table_headers= r['resultSet']['headers']


playoffs_url = 'https://stats.nba.com/stats/leagueLeaders?ActiveFlag=No&LeagueID=00&PerMode=Totals&Scope=S&Season=All%20Time&SeasonType=Playoffs&StatCategory=PTS'
p = requests.get(url=playoffs_url).json()


all_regular_data = pd.DataFrame(r['resultSet']['rowSet'],columns=table_headers)
all_playoffs_data = pd.DataFrame(p['resultSet']['rowSet'],columns=table_headers)



single_player_regular_data = 0
single_player_playoff_data = 0



def obtainRegularSeasonDataForPlayer(ID):
    global single_player_regular_data
    single_player_regular_data = all_regular_data.loc[all_regular_data['PLAYER_ID'] == ID]




def obtainPlayoffsDataForPlayer(ID):
    global single_player_playoff_data
    single_player_playoff_data = all_playoffs_data.loc[all_playoffs_data['PLAYER_ID'] == ID]





def RegularSeasonGamesPlayed(ID):
    obtainRegularSeasonDataForPlayer(ID)
    GPSeries = single_player_regular_data['GP'].item()
    print(GPSeries)
    print("that was regular season")
    return GPSeries



def PlayoffGamesPlayed(ID):
    obtainPlayoffsDataForPlayer(ID)
    GPSeries = single_player_playoff_data['GP'].item()
    print(GPSeries)
    print("That was playoffs")
    return GPSeries



def RegularFG(ID):
    GPSeries = single_player_regular_data['FG_PCT'].item()
    return GPSeries


def PlayoffsFG(ID):
    GPSeries = single_player_playoff_data['FG_PCT'].item()
    return GPSeries



def Regular3PointFG(ID):
    GPSeries = single_player_regular_data['FG3_PCT'].item()
    return GPSeries


def Playoffs3PointFG(ID):
    GPSeries = single_player_playoff_data['FG3_PCT'].item()
    return GPSeries



def RegularFreeThrow(ID):
    GPSeries = single_player_regular_data['FT_PCT'].item()
    return GPSeries


def PlayoffsFreeThrow(ID):
    GPSeries = single_player_playoff_data['FT_PCT'].item()
    return GPSeries




def RegularTotalPoints(ID):
    GPSeries = single_player_regular_data['PTS'].item()
    return GPSeries


def PlayoffsTotalPoints(ID):
    GPSeries = single_player_playoff_data['PTS'].item()
    return GPSeries





def RegularAssists(ID):
    GPSeries = single_player_regular_data['AST'].item()
    return GPSeries


def PlayoffsAssists(ID):
    GPSeries = single_player_playoff_data['AST'].item()
    return GPSeries



def RegularRebounds(ID):
    GPSeries = single_player_regular_data['REB'].item()
    return GPSeries


def PlayoffsRebounds(ID):
    GPSeries = single_player_playoff_data['REB'].item()
    return GPSeries




def RegularTurnovers(ID):
    GPSeries = single_player_regular_data['TOV'].item()
    return GPSeries


def PlayoffsTurnovers(ID):
    GPSeries = single_player_playoff_data['TOV'].item()
    return GPSeries




def RegularBlocks(ID):
    GPSeries = single_player_regular_data['BLK'].item()
    return GPSeries


def PlayoffsBlocks(ID):
    GPSeries = single_player_playoff_data['BLK'].item()
    return GPSeries




def RegularSteals(ID):
    GPSeries = single_player_regular_data['STL'].item()
    return GPSeries


def PlayoffsSteals(ID):
    GPSeries = single_player_playoff_data['STL'].item()
    return GPSeries




def RegularMinutes(ID):
    GPSeries = single_player_regular_data['MIN'].item()
    return GPSeries


def PlayoffsMinutes(ID):
    GPSeries = single_player_playoff_data['MIN'].item()
    return GPSeries




















