#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
#------------------------------------------#

# -- DATA -- #
import pickle
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
    """
    @staticmethod
    def add_CD(newCD):
        """adds your newCD arguments by way of get_CD function to the list table"""
        lstOfCDObjects.append(newCD)
        IO.show_inventory(lstOfCDObjects)
       
    @property
    def cd_id(self):
        """property to return cd id"""
        return self.__cd_id

    @property
    def cd_title(self):
        """allows return of CD title"""
        return self.__cd_title
    
    @property
    def cd_artist(self):
        """property to return artist of the CD"""
        return self.__cd_artist
    
    #REQUIRED constructor to instantiate the object and the data members of the class: the properties we were already given  
    def __init__(self, id, title, artist):
        """creates a cd class using the three parameters we have"""
        self.__cd_id = id
        self.__cd_title = title
        self.__cd_artist = artist
        

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    (move and utilize previous SAVE/LOAD routines?)
    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    @staticmethod
    def save_CD(file_name, lst_Inventory):
        """saves CD data to default CDInventory.txt file name"""
        with open(strFileName, 'wb') as fileObj:
            pickle.dump(lstOfCDObjects, fileObj)
            """when using pickling function, data is saved properly in binary when checking the file created"""
            
    @staticmethod
    def load_inventory(file_name):
        """do i need to reconnect a read_file function in order to make my 
        load inventory function properly compared to what is expected normally?"""
        with open(file_name, 'rb') as fileObj:
            lstOfCDObjects.clear() #clear the list
            freshTable = None
            try:
                freshTable = pickle.load(fileObj)    
                for i in range(0, len(freshTable)):
                    lstOfCDObjects.append(freshTable[i]) 
            except Exception as e:
                    """fixing error/issue with a blank inventory file loading in"""
                    print('\nProgram started, but nothing was loaded...\n')
                    print(type(e), e, e.__doc__, sep='\n')
            except FileNotFoundError as e:
                print("Unable to find the specified filename")
                print(type(e), e, e.__doc__, sep='\n')
            """pickled object definitely exists as a list(?) but does not display/load properly outside of this print"""    

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    """Able to reutilize old assignment methods to create and show menu to user, including menu choice, display options, and 
    fetch CD using ID parameter"""
    # TODO add code to show menu to user
    # TODO add code to captures user's choice
    # TODO add code to display the current data on screen
    # TODO add code to get CD data from user
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        
        """no delete option asked for, safe to remove d as a list option"""
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
        
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            """no delete option asked for, safe to remove d as a choice"""
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice    

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            """if keeping CD as upper case, will it refer to the class we already have or the object in the table?"""
            print('{}\t{} (by:{})'.format(cd.cd_id, cd.cd_title, cd.cd_artist))
        print('======================================')
        
    @staticmethod
    def get_CD():
        """Asks for inventory specifications with the three specified parameters"""
        while True:
            try:
                strID = int(input('Enter ID: ').strip())
                break
                """requires a loop to avoid continuing asking for other inputs and restarts at asking for ID again"""
            except ValueError as e:
                print('That is not an integer!\n')
                print(type(e), e, e.__doc__, sep='\n')    
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        """changed returning dictionary list to returning the specific CD properties""" 
        return CD(strID, strTitle, strArtist)   
    
# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start

FileIO.load_inventory(strFileName)

# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    if strChoice == 'x':
        break
    if strChoice == 'a':
        newerCD = IO.get_CD()
        CD.add_CD(newerCD)
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_CD(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')   
        continue  
    elif strChoice == 'l':
        FileIO.load_inventory(strFileName)    
    else:
        print('General Error')
