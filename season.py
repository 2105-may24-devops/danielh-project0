import league_mgmt
import file_mgmt
import random

def sim_season(league_name):
    game_log = None
    #season_length = league_name
    league_size = file_mgmt.get_leagueSize(league_name)
    teams = file_mgmt.get_teams(league_name)
    team_info = file_mgmt.get_teamInfo(league_name)
    team_info_t= [tuple(map(str, sub.split(', '))) for sub in team_info]
    range_m = list(range(0,league_size))
    sample = random.sample(range_m, 1)
    winner = team_info_t[sample[0]][0]
    winner = winner.partition("Team Name: ")[2]
    #print(winner)
    return winner
    
    pass

def game(teamA, teamB):

    pass