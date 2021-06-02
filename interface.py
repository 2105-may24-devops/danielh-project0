import file_mgmt
import league_mgmt
import menu
import settings
class interface():
    menu_option = "0"
    league = None
    league_info = None
    league_list = None
    league_name = None
    pass

    def run_interface(self):
        file_mgmt.create_home()
        while self.menu_option != "4":
            #Main Menu System
            if self.menu_option == "0":
                self.menu_option = menu.run_menus(self.menu_option)

            #Create a League Menu System
            elif self.menu_option == "1":
                self.league_info = menu.run_menus(self.menu_option)
                print(self.league_info)
                name, size = self.league_info
                league = league_mgmt.league(name,size)
                league.create_league()
                league.populate_league()
                self.menu_option = "0"
            #Load a League Menu
            elif self.menu_option == "2":
                #league_list = file_mgmt.get_leagues()
                self.league_name = menu.run_menus(self.menu_option)
                self.menu_option = "3"
            elif self.menu_option == "3":
                menu.run_menus(self.menu_option)
                pass
        print(self.league_name)    
        #pass