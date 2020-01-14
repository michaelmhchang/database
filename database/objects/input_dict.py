import csv
from .item import item, price

def in_dict(item_dict, rows):

    # Organize each list to each item
    organized_items = []

    # Creating a list per item to input info
    for i in range(int(len(rows[0])/2)):
        organized_items.append([])  

    keys = rows.pop(0)

    for col in range(int(len(rows[0])/2)):
            for row in rows:
                organized_items[col].append(row[col*2])
                organized_items[col].append(row[col*2+1])

    for o in organized_items:
        o[:] = [i for i in o if i != ' ']

    for k in range(0, int(len(keys)/2)):
        item_dict[(keys[k*2],keys[k*2+1])] = []

        for p_info in range(int(len(organized_items[k])/2)):
            p = price(organized_items[k][p_info*2+1])
            p.date = organized_items[k][p_info*2]

            item_dict[(keys[k*2],keys[k*2+1])].append(p)

    return(item_dict)

