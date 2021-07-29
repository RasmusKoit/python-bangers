
"""
    ---------------------------------------------------------------------------------------------------------
    Your coworker started his own company and he has a lot of tools, 
    bits and bobs and he would like to have a little system to show him what he has in his shed.
    He has given you a list of tools and other things he has and has already categorized them

    He would also be very glad to get some small statistics and calculations related to his tools and things
    ---------------------------------------------------------------------------------------------------------

    TASK:
    Please print out how many total different things does have in his inventory (ignore amount)
    # example output
    Coworker bob has 9 things in his inventory

    TASK:
    Please print out how many different types of items Bob has and list the item types
    # example output
    tool: 3
    material: 2
    metal: 2
    misc: 2

    TASK:
    Please write program that shows total amount of every item bob has (including items that don't specifiy amount)
    # example output
    Bob has total of 215 items

    TASK:
    Please write a program that shows his different type of items and amounts if specified, if amount isnt specified, just write 1 instead.
    # example output
    Item type: Tool
    Item name: hammer, 1
    Item name: saw, 1
    Item name: mallet, 1

    Item type: Material
    Item name: nails, 100
    Item name: bolts, 50

    Item type: Metal
    Item name: iron, 54
    Item name: Aluminium, 30

    Item type: Misc
    Item name: beers, 6
    Item name: Spraypaint, 2

"""

from typing import List, Dict

def countItemTypes(dictionaryList: List[Dict]):
    totalItems = 0
    # your code here

    return str(totalItems)


if __name__ == "__main__":
    
    inventoryList = [
        {
            "name": "hammer",
            "type": "tool",        
        },
        {
            "name": "saw",
            "type": "tool",
        },
        {
            "name": "mallet",
            "type": "tool",
        },
        {
            "name": "nails",
            "type": "material",
            "amount": 100
        },
        {
            "name": "bolts",
            "type": "material",
            "amount": 50
        }, 
        {
            "name": "iron",
            "type": "metal",
            "amount": 54
        },
        {
            "name": "aluminium",
            "type": "metal",
            "amount": 30
        },
        {
            "name": "beers",
            "type": "misc",
            "amount": 6
        },
        {
            "name": "spraypaint",
            "type": "misc",
            "amount": 2
        }
    ]

    # Task 1 output
    print("Bob has total of " + countItemTypes(inventoryList) + " items")