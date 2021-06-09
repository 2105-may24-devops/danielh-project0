from pathlib import Path
from team_mgmt import team
import settings
import os
from datetime import datetime
homedir = settings.homedir


# Create home directory within which all other game dir/files are stored
# if home dir exists welcome back user
def create_home():
    now = datetime.now()
    try:
        Path(f"./{homedir}").mkdir(parents=True)
        with open(f"./{homedir}/info.txt", "a+") as f:
            f.write("This is the home directory, in which all league files are stored.")
        with open(f"./{homedir}/log.txt", "a+") as f:
            f.write(f"Most recent run: {now}")  
    except FileExistsError:
        #print("Welcome back!")
        with open(f"./{homedir}/log.txt", "r+") as f:
            content = f.read()
            f.seek(0, 0)
            f.write(f"Most recent run: {now} \n{content}")
        pass
   
# Create directory
# If directory exists return false
def create_dir(name, size, filetype):
    try:
        Path(f"./{homedir}/{name}").mkdir(parents=True)
        with open(f"./{homedir}/{name}/league_info.txt", "a+") as f:
            f.write(f"League Name: {name}, Size: {size} ")
    except FileExistsError:
        return False

# Create team director within given league
def create_team_file(league_name, team_name, team_rating):
    this_team = team(team_name, team_rating)
    try:
        Path(f"./{homedir}/{league_name}/{team_name}").mkdir(parents=True)
        with open(f"./{homedir}/{league_name}/{team_name}/team_info.txt", "a+") as f:
            f.write(str(this_team))
    except FileExistsError:
        return False
    pass

def print_leagues():
    leagues = next(os.walk(f'./{homedir}'))[1]
    print(leagues)

def get_leagues():
    leagues = next(os.walk(f'./{homedir}'))[1]
    return leagues

def print_teams(league):
    teams = next(os.walk(f'./{homedir}/{league}'))[1]
    print(teams)

def get_teams(league):
    teams = next(os.walk(f'./{homedir}/{league}'))[1]
    return teams

def get_teamInfo(league):
    teams = get_teams(league)
    team_info = []
    for team in teams:
        with open(f'./{homedir}/{league}/{team}/team_info.txt', 'r') as fin:
            team_info.append(fin.read())
    return team_info
    
def get_leagueSize(league):
    league_info = None
    with open(f"./{homedir}/{league}/league_info.txt", "r") as f:
            league_info = f.read()
    size = int(league_info.partition("Size: ")[2])
    return size