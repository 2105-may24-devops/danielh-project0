import file_mgmt
import settings
import random

class team:

    def __init__(self, name, league):
        self.name = name
        self.league = league
        self.rating = int(random.random()*10+1)
    def create_team(self):
        file_mgmt.create_team_file(self.league, self.name, self.rating)
        pass
        
        
