from collections import namedtuple
import file_mgmt

#class definition for Menu
class Menu:
    Option = namedtuple('option', 'label')
    _separator = "=" * 25
    _main_options = {"1": Option("Create New League"), "2": Option("Load League"), 
    "9": Option("Exit")}
    _league_options = {"1": Option("View Teams"),"2": Option("Simulate Season"), 
    "0": Option("Return to Main Menu")}
    current_menu = "0"

<<<<<<< HEAD
    #MENU SELECTOR
    #Handles selection of desired menu
    #prints selected menu
=======
    #Method for geting user input and running features
>>>>>>> 72f05ec70a1fe69e5c1068c8257a249f966fa045
    def menu_selector(self, menu_selection):
        self.current_menu = menu_selection
        if self.current_menu == "0":
            self.print_mainMenu()
        elif self.current_menu == "1":
            self.print_createLeagueMenu()
        elif self.current_menu == "2":
            self.print_loadLeagueMenu()
        elif self.current_menu == "3":
            self.print_leagueMenu()
            pass
<<<<<<< HEAD

    

    #MAIN MENU

    #Prints the header for the main menu
    def print_mainHeader(self):
        print("\n{0}\n Please Select an Option\n{0}".format(self._separator))

    #Prints the main menu, listing available options
=======
    
    #print main header display
    def print_mainHeader(self):
        print("\n{0}\n Please Select an Option\n{0}".format(self._separator))

    #method for printing main menu
>>>>>>> 72f05ec70a1fe69e5c1068c8257a249f966fa045
    def print_mainMenu(self):
        self.print_mainHeader()
        for option in sorted(self._main_options.keys()):
            print ("{0} {1}".format(option, self._main_options[option].label))
<<<<<<< HEAD

    #Input prompt for user to select option from main menu
    def main_prompt(self):    
        return input("Select Option: ")
        
    #Handles the input for a selection from main menu, and returns selection
    #If invalid option entered, notify user
    def handle_main_input(self, chosen_option):
        try:
            print (self._main_options[chosen_option].label)
            return chosen_option
        except KeyError:
            print ("Invalid Option")

    #CREATE LEAGUE MENU

    #Prints header for create a league menu
    def print_createLeagueMenu(self):
        print("\n{0}\n Create a League\n{0}".format(self._separator))
        pass

    #Prompts user for input: name and size for league to be created
    #Return input as tuple
=======
    #print menu for League creation 
    def print_createLeagueMenu(self):
        print("\n{0}\n Create a League\n{0}".format(self._separator))
        pass
    #print loading menu
    def print_loadLeagueMenu(self):
        pass
    #Method for getting user input for League information 
>>>>>>> 72f05ec70a1fe69e5c1068c8257a249f966fa045
    def create_prompt(self):
        league_input = ()
        league_input = tuple(input("Please enter a name and size for your league: ").split(","))
        return league_input
<<<<<<< HEAD

    
=======
    #method for getting user input for menu
    def main_prompt(self):    
        return input("Select Option: ")
    #Method for selecting Leagues
    def league_prompt(self):
        print(file_mgmt.get_leagues())
        return input("Select League: ")
    #Error handling for user input
    def handle_input(self, chosen_option):
        try:
            print (self._main_options[chosen_option].label)
            return chosen_option
        except KeyError:
            print ("Invalid Option")
>>>>>>> 72f05ec70a1fe69e5c1068c8257a249f966fa045
    
    #LEAGUE SELECTOR MENU

    #Prompts user to select league from list of all created leagues
    def choose_league_prompt(self):
            print(file_mgmt.get_leagues())
            return input("Select League: ")

    #Handles selection of league to load
    #If selection invalid, notify user
    def handle_league_selection(self, chosen_option):
        options = file_mgmt.get_leagues()
        try:
            if chosen_option in options:
                return chosen_option
        except:
            print ("Invalid Option")
    
    

    def print_loadLeagueMenu(self): 
        pass
<<<<<<< HEAD

    #LEAGUE MENU

    #Prints header for League Menu
    def print_leagueHeader(self):
        print("\n{0}\n League Menu\n{0}".format(self._separator))

    #Prints options for league menu
    def print_leagueMenu(self):
        self.print_leagueHeader()
        for option in sorted(self._league_options.keys()):
            print ("{0} {1}".format(option, self._league_options[option].label))
    
    #Handles input for selection within league menu
    #If selection invald, notify user
    def handle_league_input(self, chosen_option):
        try:
            print (self._league_options[chosen_option].label)
            return chosen_option
        except KeyError:
            print ("Invalid Option")
    

#Handles running the menus by calling menu_selector method
#runs desired menu and returns output from running the menu
=======
#Method for starting menu display and electin process
>>>>>>> 72f05ec70a1fe69e5c1068c8257a249f966fa045
def run_menus(menu_selection):
    menu = Menu()
    menu.menu_selector(menu_selection)
    if menu_selection == "0":
        return menu.handle_main_input(menu.main_prompt())
    if menu_selection == "1":
        return menu.create_prompt()
    if menu_selection == "2":
        return menu.handle_league_selection(menu.choose_league_prompt())
    if menu_selection == "3":
        return menu.handle_league_input(menu.main_prompt())
        pass

