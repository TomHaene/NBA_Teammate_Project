from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
from nba_api.stats.static import players, teams
import pandas as pd
from nba_api.stats.endpoints import playergamelog, teamgamelog, leaguegamefinder, commonplayerinfo, commonallplayers
from nba_api.stats.library.parameters import SeasonAll


all_players_dict = players.get_players()
nba_players_df = pd.DataFrame(all_players_dict)


everyPlayerIDandName = {}

everyPlayerName = everyPlayerIDandName.values()



for player in all_players_dict:
    player_id = player['id']
    player_name = player['full_name']
    everyPlayerIDandName[player_id] = player_name
    


for player in all_players_dict:
   player_id = player['id']
   player_name = player['full_name']
   everyPlayerIDandName[player_id] = player_name

 











