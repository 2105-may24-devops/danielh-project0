from typing import Sized
import file_mgmt
import settings
import team_mgmt
import random

class league:

    def __init__(self, name, size):
        self.name = name
        self.size = size

        #self.create_league()
        
    #Takes in str name as name of league to be created
    #If league with that name already exists, notify user
    def create_league(self):
        if file_mgmt.create_dir(self.name, "league") == False:
            print("League with that name already exists.")
        

    def populate_league(self):
        rangemax = list(range(0, len(settings.team_names)))
        sample = random.sample(rangemax, int(self.size))
        print(sample)
        for i in sample:
            team = team_mgmt.team(settings.team_names[i], self.name)
            team.create_team()
        pass