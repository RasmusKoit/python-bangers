"""
    Mari wants to make a simple terminal based book information app.
    Since she has so many books, she wants to quickly browse all the books.
    
    While browsing books there should title with initials displayed as shown below
    Harry Potter: Python Masters - J.K.R.
    
    
    Please store the initial information about each book in dictionary format
    book = {
        "title": <str>,
        "author": <str>,
        "released": <int>,
        "pages": <int>
    }
    
    Mari wants to be able to get more information about a specific book so please show it to her.
    This means that mari will get a list of books with numbers infront and by specifing a number
    she will be able to see some more information about it. 
    
    
    1. book Y
    2. book X
    3. book Z
    
    0. close menu
    Which book would you like to see (0 to close menu): 2
    
    Book X by A. B. Bowanga - 1996
    Pages: 222
    
    
    Mari likes to manage her time a lot and she knows that her median reading speed is 3.5 minutes
    When displaying book information add information that would show her how many hours it would take her
    to finish reading the book (round the time up if needed)
    
    Book X by A. B. Bowanga - 1996
    Pages: 222
    Reading time: 13 hours
    
"""

book1 = {
    "title": "Ott the Ribbit",
    "author": "Franz Gründinand",
    "released": 1888,
    "pages": 12,
    }

book2 = {
    "title": "Narnia: the magical closet",
    "author": "Rasmussen Kult",
    "released": 2000,
    "pages": 199,
    }

book3 = {
    "title": "Hobbit and the 12 Bro's",
    "author": "Heinrich Rolf Torpa",
    "released": 1922,
    "pages": 355,
    }

# see sitt peab tekitama nimekirja raamatupealkirjadest

bookList = [book1, book2, book3]

# funktsiooni mis suudab võtta 'bookList'ist välja ühe raamatu ja kuvada pealkirja
# funktsioon peab läbi käima kõik raamatud, ja iga raamatu kohta kuvama raamatu pealkirja


def initialMaker(book):
    # 1. split authors name into list
    # 2. show 1st letter of each name
    # 3. add (.) after each letter
    # 4. after doing step 2 and 3 add initial to empty string
    # 5. return final string

    authorstr = (book.get("author"))

    authorNameList = authorstr.split()
    


    
    # return answer


def displayBookTitle(bookList):
    for book in bookList:
        # print(book.get("title"))

        print(initialMaker(book))
displayBookTitle(bookList)

# autori nime initsiaalide teke



    



