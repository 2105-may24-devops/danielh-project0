from pathlib import Path
from team_mgmt import team
import settings
import os
homedir = settings.homedir

# Create home directory within which all other game dir/files are stored
# if home dir exists welcome back user
def create_home():
    try:
        Path(f"./{homedir}").mkdir(parents=True)
        with open(f"./{homedir}/info.txt", "a+") as f:
            f.write("This is the home directory, in which all league files are stored.")
    except FileExistsError:
        #print("Welcome back!")
        pass
   
# Create directory
# If directory exists return false
def create_dir(name, filetype):
    try:
        Path(f"./{homedir}/{name}").mkdir(parents=True)
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

    
            