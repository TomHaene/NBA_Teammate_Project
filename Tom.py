#This file will contain the code for the display of the shot data in the regular season and in the playoffs
from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats.static import players, teams
import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguegamefinder, commonplayerinfo, commonallplayers
from nba_api.stats.library.parameters import SeasonAll

from nba_api.stats.endpoints import playercareerstats


def getAllPlayersList():
    all_players_dict = players.get_players()
    nba_players_df = pd.DataFrame(all_players_dict)
    firstLast_df = nba_players_df['full_name']
    firstLast_list = firstLast_df.tolist()
    return firstLast_list




def setup(name):
  
    playerName = name.title()
  

    if(playerName == "Lebron James"):
        playerName = "LeBron James"
    
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




def RegularSeasonGamesPlayed(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_regular_season
    regularDFBron = regularSeasonTotalsDataSet.get_data_frame()
    if (regularDFBron.empty):
      
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
    
        return 0
    playoffsFGBron = playoffsDFBron['GP']
     
    GPPlayoffs = playoffsFGBron.item()

    print(GPPlayoffs)
 

    return GPPlayoffs


def seasonsMadePlayoffs(playerID):
     # Create an instance of the PlayerCareerStats endpoint
    player_stats = playercareerstats.PlayerCareerStats(player_id=playerID)

    # Retrieve the player's career stats data
    career_stats = player_stats.get_data_frames()[0]

    # Filter the career stats data to get the seasons where the player played in the playoffs
    playoff_seasons = career_stats[career_stats['SEASON_TYPE'] == 'Playoffs']['SEASON_ID']

    # Print the list of playoff seasons
    

    return playoff_seasons




def seasonsPlayedOverall(playerID):
    
    # Create an instance of the PlayerCareerStats endpoint
    player_stats = playercareerstats.PlayerCareerStats(player_id=playerID)

    # Retrieve the player's career stats data
    career_stats = player_stats.get_data_frames()[0]

    # Filter the career stats data to get the seasons where the player played in the playoffs


    seasons = career_stats[career_stats['PTS'] > 0]['SEASON_ID']

    # Print the list of playoff seasons
   
    return seasons



def RegularFG(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_regular_season
    regularDFBron = regularSeasonTotalsDataSet.get_data_frame()
    regularFGBron = regularDFBron['FG_PCT']
    FGregularSeason = regularFGBron.item()
  
    return FGregularSeason


def PlayoffsFG(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['FG_PCT']
    FGplayoffs = playoffsFGBron.item()
    
    return FGplayoffs




def Regular3pointfg(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_regular_season
    regularDFBron = regularSeasonTotalsDataSet.get_data_frame()
    regularFGBron = regularDFBron['FG3_PCT']
    threeFGregularSeason = regularFGBron.item()

    return threeFGregularSeason



def Playoffs3pointfg(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['FG3_PCT']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs







def RegularFreeThrow(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    regularSeasonTotalsDataSet = careerStats.career_totals_regular_season
    regularDFBron = regularSeasonTotalsDataSet.get_data_frame()
    regularFGBron = regularDFBron['FT_PCT']
    threeFGregularSeason = regularFGBron.item()
    

    return threeFGregularSeason



def PlayoffsFreeThrow(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['FT_PCT']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs





def regularShotChartSeasonal(playerID, season):
    shot_chart = ShotChartDetail(player_id = playerID, team_id=0, season_nullable=season, context_measure_simple = 'FGA', season_type_all_star = 'Regular Season')
    shot_data = shot_chart.get_data_frames()[0]
    return shot_data



# We're gonna want to call the above function for all the times that the given player made the playoffs.
# Since we can only obtain the shot data on a seasonal basis



def playoffsShotChartSeasonal(playerID, season):
    shot_chart = ShotChartDetail(player_id = playerID, team_id=0, season_nullable=season, context_measure_simple = 'FGA', season_type_all_star = 'Playoffs')
    shot_data = shot_chart.get_data_frames()[0]
    return shot_data
    


def regularTotalPoints(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_regular_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['PTS']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs


def playoffsTotalPoints(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['PTS']
    threeFGplayoffs = playoffsFGBron.item()


    return threeFGplayoffs




def regularTotalAssists(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_regular_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['AST']
    threeFGplayoffs = playoffsFGBron.item()
 
    return threeFGplayoffs


def playoffsTotalAssists(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['AST']
    threeFGplayoffs = playoffsFGBron.item()
    

    return threeFGplayoffs


def regularTotalRebounds(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_regular_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['REB']
    threeFGplayoffs = playoffsFGBron.item()
  
    return threeFGplayoffs


def playoffsTotalRebounds(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['REB']
    threeFGplayoffs = playoffsFGBron.item()
  

    return threeFGplayoffs


def regularTotalTurnovers(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_regular_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['TOV']
    threeFGplayoffs = playoffsFGBron.item()
    print(threeFGplayoffs)
    
    return threeFGplayoffs


def playoffsTotalTurnovers(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]

    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()

    playoffsFGBron = playoffsDFBron['TOV']
    threeFGplayoffs = playoffsFGBron.item()
   

    return threeFGplayoffs







def regularTotalBlocks(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_regular_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['BLK']
    threeFGplayoffs = playoffsFGBron.item()
   
    return threeFGplayoffs


def playoffsTotalBlocks(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['BLK']
    threeFGplayoffs = playoffsFGBron.item()

    return threeFGplayoffs



def regularTotalSteals(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_regular_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['STL']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs


def playoffsTotalSteals(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['STL']
    threeFGplayoffs = playoffsFGBron.item()
  

    return threeFGplayoffs



def regularTotalMinutes(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_regular_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['MIN']
    threeFGplayoffs = playoffsFGBron.item()
    
    return threeFGplayoffs


def playoffsTotalMinutes(playerID):
    careerStats = playercareerstats.PlayerCareerStats(player_id = playerID)
    career_stats_data = careerStats.get_data_frames()[0]
    playoffsTotalsDataSet = careerStats.career_totals_post_season
    playoffsDFBron = playoffsTotalsDataSet.get_data_frame()
    playoffsFGBron = playoffsDFBron['MIN']
    threeFGplayoffs = playoffsFGBron.item()

    return threeFGplayoffs
