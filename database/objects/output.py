from .item import item, price
from copy import deepcopy
import csv

def max_count(lst_of_prices):
    count = 0

    for p in lst_of_prices:
        count = max(count, len(p))

    return(count)

# Updates item_dict 
def append_dic(item_dict, item):

    # If item is already in the dictonary, append new price
    if (item.name, item.upc) in item_dict:
        item_dict[(item.name, item.upc)].append(item.prices[0])

    # Else append new item value into item dictionary (the dictionary is empty) 
    else:
        item_dict[(item.name,item.upc)] = item.prices

    return(item_dict)


# Outputs it to csv
def output(item_dict, item):
    csvFile = open('database.csv', 'w')
    writer = csv.writer(csvFile)

    keys = []

    # Getting the keys into one list for the title row
    for k in item_dict.keys():
        keys.append(k)

    # Making the rows for the output, which start with the keys as the title 
    titles = []

    for key in keys:
        titles.append(key[0])
        titles.append(key[1])

    rows = [[titles]]

    # List of the dictionary values (which are the prices)
    # ***Deepcopy because I don't want it to change the actual value in the dictionary
    prices_holder = deepcopy(list(item_dict.values()))

    # Organizing the prices_holder list so that it outputs correctly into rows and rowumns
    ordered_prices = []

    # Max amount of prices in a list of prices
    max_prices = max_count(prices_holder)

    for ordered_rows in range(max_prices):
        ordered_prices.append([])

    # Instead of popping out the element to check for blank list, fill in the list with blank spaces from the start

    for prices in prices_holder:
        while len(prices) != max_prices:
            prices.append(' ')

    for row in range(len(ordered_prices)):
        for p in prices_holder:
            if p[row] == ' ':
                ordered_prices[row].append(' ')
                ordered_prices[row].append(' ')
            else:
                ordered_prices[row].append(p[row].date)
                ordered_prices[row].append(p[row].amount)
    
    rows.append(ordered_prices)

    for row in rows:
        writer.writerows(row)

    csvFile.close()


