from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
import numpy as np
from math import pi
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import LeagueGameFinder

import urllib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc

from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats.static import players, teams
import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguegamefinder, commonplayerinfo, commonallplayers
from nba_api.stats.library.parameters import SeasonAll

from nba_api.stats.endpoints import playercareerstats





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

def seasonsPlayedOverall(playerID):
    
    # Create an instance of the PlayerCareerStats endpoint
    player_stats = playercareerstats.PlayerCareerStats(player_id=playerID)

    # Retrieve the player's career stats data
    career_stats = player_stats.get_data_frames()[0]

    # Filter the career stats data to get the seasons where the player played in the playoffs
    seasons = career_stats[career_stats['PTS'] > 0]['SEASON_ID']

    # Print the list of playoff seasons

    return seasons


def playoffsThatYear(playerID, season):
    gamelog = playergamelog.PlayerGameLog(player_id=ID, season_type_all_star='Playoffs', season=season)
     
    # Get player's game logs for playoffs
    gamelog_data = gamelog.get_data_frames()[0]
     
    # Extract the playoff season information
    playoff_season = gamelog_data["SEASON_ID"].unique()
     
    # Print the playoff seasons
    if (gamelog_data.empty):
        return False
    else:
        return True
        
    

def playoffSeasonsPlayed(playerID):
    #iterate over all the years that a player has played
    totalPlayoffSeasons = []
    for season in seasonsPlayedOverall(playerID):
        if(playoffsThatYear(playerID, season)):
            totalPlayoffSeasons.append(season)

    return totalPlayoffSeasons






# def regularShotChartSeasonal(playerID, season):
#     shot_chart = ShotChartDetail(player_id = playerID, team_id=0, season_nullable=season, context_measure_simple = 'FGA', season_type_all_star = 'Regular Season')
#     complex_shot_data = shot_chart.get_data_frames()[0]
#     shot_location_data = complex_shot_data[['LOC_X', 'LOC_Y']]

#     return shot_location_data




# def totalRegularShotChart(playerID):  
#     totalRegularShotLocationData=pd.DataFrame()
#     for season in seasonsPlayedOverall(playerID).tolist():
#         print(season)
#         shot_data = regularShotChartSeasonal(playerID, season)
#         totalRegularShotLocationData = pd.concat([totalRegularShotLocationData, shot_data])
#         shot_location_list= totalRegularShotLocationData.values.tolist()

#     return shot_location_list



# def playoffShotChartSeasonal(playerID, season):
#     shot_chart = ShotChartDetail(player_id = playerID, team_id=0, season_nullable=season, context_measure_simple = 'FGA', season_type_all_star = 'Playoffs')
#     complex_shot_data = shot_chart.get_data_frames()[0]
#     shot_location_data = complex_shot_data[['LOC_X', 'LOC_Y']]

#     return shot_location_data




# def totalPlayoffShotChart(playerID):  
#     totalRegularShotLocationData=pd.DataFrame()
#     for season in seasonsPlayedOverall(playerID).tolist():
#         print(season)
#         shot_data = regularShotChartSeasonal(playerID, season)
#         totalRegularShotLocationData = pd.concat([totalRegularShotLocationData, shot_data])
#         shot_location_list= totalRegularShotLocationData.values.tolist()

#     return shot_location_list







