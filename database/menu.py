import objects.database as database 
import objects.item as item
import os,sys
import csv

class Menu:
    def __init__(self):
        self.database = database.database()
        self.choices = {
                "1" : self.database.show_items,
                "2" : self.database.add_item,
                "3" : self.quit
                }
    
    def display_menu(self):
        print("""
        Walmart database menu

        1. Show database
        2. Add item 
        3. Quit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            print('\n')
            action = self.choices.get(choice)
            if action:
                os.system('clear')
                action()
            else:
                print("{0} is not a valide choice".format(choice))

    def quit(self):
        print("Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
