import file_mgmt
import league_mgmt
import menu
import settings
import season
class interface():
    menu_option = "0"
    league = None
    league_info = None
    league_list = None
    league_name = None
    l_menu_option = None
    selected_league = None
    pass

    def run_interface(self):
        file_mgmt.create_home()
        while self.menu_option != "9":
            #Main Menu System
            if self.menu_option == "0":
                self.menu_option = menu.run_menus(self.menu_option)

            #Create a League Menu System
            elif self.menu_option == "1":
                self.league_info = menu.run_menus(self.menu_option)
                #print(self.league_info)
                try:
                    name, size = self.league_info
                    league = league_mgmt.league(name,size)
                    league.create_league()
                    league.populate_league()
                    print("League created.")
                except ValueError:
                    print("Invalid Input. Example: 'league, 12' ")
                    self.menu_option = "0"
                
                self.menu_option = "0"
            #Load a League Menu
            elif self.menu_option == "2":
                #league_list = file_mgmt.get_leagues()
                self.league_name = menu.run_menus(self.menu_option)
                if self.league_name == None:
                    print("Invalid selection.")
                    self.menu_option == "2"
                else:
                    self.menu_option = "3"
            #Within a League Menu
            elif self.menu_option == "3":
                #print(self.league_name)
                self.l_menu_option = menu.run_menus(self.menu_option, self.league_name)
                if self.l_menu_option == "0":
                    self.menu_option = "0"
                elif self.l_menu_option == "1":
                    info = file_mgmt.get_teamInfo(self.league_name)
                    print(('\n'.join(map(str, info))))
                    pass
                elif self.l_menu_option == "2":
                    winner = season.sim_season(self.league_name)
                    print(f"Season Winner: {winner}")
        #print(self.league_name)    
        #pass