from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
inv_length = len(inventory)
current_room = rooms["Reception"]
current_mass = 0

def calc_mass(inventory):
    for x in range(0, inv_length):
        mass = 0
        mass += inventory[x]["mass"]

    return(mass)

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_mass = calc_mass(inventory)
    
