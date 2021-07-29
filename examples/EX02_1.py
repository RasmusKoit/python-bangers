from typing import Dict, List

def welcome(companyName, sellersName: str):
    print("""Welcome to {}! Buy your new home from us 
and participate in a brand new Toyota RAV4 giveaway!""".format(companyName))

    customerName = input("Hiya there person, my name is:{}".format(sellersName))

    print("Would you like to see our new apartment listings, {}?".format(customerName))

    getConfirmation()

def displayApartments(listOfApartments: List[Dict]):
    print("We have total of {} apartments listed".format(len(listOfApartments)))
    for apartment in listOfApartments:
        apartmentText = getApartmentInfo(apartment)
        getConfirmation()
        print(apartmentText)

def getApartmentInfo(apartment: Dict) -> str:
    info = """
Street: {},
City: {},
County: {},
Rooms: {},
Size: {} sq/ft,
Price: {}€1
    """.format(apartment.get("street", ""),
               apartment.get("city", ""),
               apartment.get("county", ""),
               apartment.get("rooms", 0),
               apartment.get("size", 0),
               apartment.get("price", 0))

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
    companyName = "Dick's"

    apt1 = {
        "street": "Liikuri",
        "city": "Tallinn",
        "county": "Harjumaa",
        "rooms": 2,
        "size": "40m2",
        "price": 144000
    }

    
    toSell = [apt1]

    sellersName = "Bezos"
    welcome(companyName, sellersName)
    displayApartments(toSell)




