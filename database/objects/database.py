import csv
import datetime
import os
import time
from .output import output, append_dic 
from .item import item, price
from .input_dict import in_dict

class database:
    def __init__(self):
        csvFile = open('database.csv')
        reader = csv.reader(csvFile, delimiter=',')

        rows = []

        for row in reader:
            rows.append(row)

        if rows:
            self.item_dict = in_dict({}, rows)

        else:
            self.item_dict = {}

        csvFile.close()

    def show_items(self):
        if self.item_dict:
            k = self.item_dict.keys()
            
            for key in k:
                print(key)
                for value in self.item_dict[key]:
                    print(str(value.date) + ' ' + value.amount)

        else:
            print("There are no items in the database!")
        
        choice = input("Press Enter to go back to the menu")
        os.system('clear')
    
    # Adds item to current dictionary + add items to the excel datasheet
    def add_item(self):
        new_item_name = input("Please enter the item's name: ")
        new_item_upc = input("Please enter the item's UPC code: ")
        new_item_price = input("Please enter the item's price: ")
       
        new_item = item(new_item_name, new_item_upc, [price(new_item_price)])

        self.item_dict = append_dic(self.item_dict, new_item)

        output(self.item_dict, new_item)

        os.system('clear')
        
