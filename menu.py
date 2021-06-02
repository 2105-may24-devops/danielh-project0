from collections import namedtuple
import file_mgmt

class Menu:
    Option = namedtuple('option', 'label')
    _separator = "=" * 25
    _main_options = {"1": Option("Create New League"), "2": Option("Load League"), 
    "3": Option("Exit")}
    _league_options = None
    current_menu = "0"

    def menu_selector(self, menu_selection):
        self.current_menu = menu_selection
        if self.current_menu == "0":
            self.print_mainMenu()
        elif self.current_menu == "1":
            self.print_createLeagueMenu()
        else:
            self.print_loadLeagueMenu()
            pass

    def print_mainHeader(self):
        print("\n{0}\n Please Select an Option\n{0}".format(self._separator))

    def print_mainMenu(self):
        self.print_mainHeader()
        for option in sorted(self._main_options.keys()):
            print ("{0} {1}".format(option, self._main_options[option].label))

    def print_createLeagueMenu(self):
        print("\n{0}\n Create a League\n{0}".format(self._separator))
        pass

    def print_loadLeagueMenu(self):
        pass

    def create_prompt(self):
        league_input = ()
        league_input = tuple(input("Please enter a name and size for your league: ").split(","))
        return league_input

    def main_prompt(self):    
        return input("Select Option: ")
    
    def league_prompt(self):
        print(file_mgmt.get_leagues())
        return input("Select League: ")
    
    def handle_input(self, chosen_option):
        try:
            print (self._main_options[chosen_option].label)
            return chosen_option
        except KeyError:
            print ("Invalid Option")
    
    def handle_league_selection(self, chosen_option):
        league_options = file_mgmt.get_leagues()
        try:
            if chosen_option in league_options:
                return chosen_option
            else:
                raise Exception
        except:
            print ("Invalid Option")

        pass

def run_menus(menu_selection):
    menu = Menu()
    menu.menu_selector(menu_selection)
    if menu_selection == "0":
        return menu.handle_input(menu.main_prompt())
    if menu_selection == "1":
        return menu.create_prompt()
    if menu_selection == "2":
        return menu.handle_league_selection(menu.league_prompt())

