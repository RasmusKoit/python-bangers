"""
Simple sales program without classes
"""

from typing import Dict, List


def welcome(name: str):
    print(
        """
Welcome to {}! We are the best store to buy what your heart desires.
My name is Rasmus, how can I be of service?
        """.format(name))
    
    customerName = input("Nice to meet you, my name is: ")
    
    print(
        "Would you like to take a look at our products, {}?".format(customerName)
    )
    getConfirmation()
    

def displayProducts(listOfProducts: List[Dict]): 
    print("We have total of {} products currently on sale!".format(len(listOfProducts)))
    for product in listOfProducts:
        productText = getProductInfo(product)
        getConfirmation()
        print(productText)


def getProductInfo(product: Dict) -> str:
    info = """
Name: {},
Price: {}€,
Year of manufactor: {},
Color: {}
    """.format(product.get("name", ""), 
               product.get("price", 0), 
               product.get("yom", 1970), 
               product.get("color", "Not specified"))
    
    return info
    

def getConfirmation():
    answer = input("Would you like to proceed? [Yes]/no")
    while(True):
        if (answer == '' or answer.lower() == 'yes'):
            return
        elif (answer.lower() == 'no'):
            print("See ya later, alligator")
            exit()
        else:
            answer = input("I am sorry, I didn't understand that, please say [yes] or no!")


if __name__ == '__main__':
    companyName = "Denny's"
    
    # This is a dictionary with "key": value
    car1 = {
        "name": "Gpad F3 MAX",
        "price": 3200,
        "yom": 2020,
        "color": "Black"
    }
    scooter1 = {
        "name": "Volvo 2",
        "price": 800,
        "yom": 1980,
        "color": "Green"
    }
    mom1 = {
        "name": "OP's mom",
        "price": 5,
        "yom": 1990,
        "color": "White"
    }
    # intentionally missing couple of fields for getProductInfo function
    gf1 = {
        "name": "Your dream GF",
        "yom": 2003
    }
    
    # List of dictionaries
    toSell = [car1, scooter1, mom1, gf1]
    
    
    welcome(companyName)
    displayProducts(toSell)
    