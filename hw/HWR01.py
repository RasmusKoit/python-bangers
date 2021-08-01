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
    
    
    Mari likes to manage her time a lot and she knows that her median reading speed is 1.7 minutes
    When displaying book information add information that would show her how many hours it would take her
    to finish reading the book (round the time up if needed)
    
    Book X by A. B. Bowanga - 1996
    Pages: 222
    Reading time: 13 hours
    
"""

from typing import Dict

READ_TIME = 1.7
BOOKS = [
    {
        "title": "Tales of the City",
        "released": 1978,
        "author": "Armistead Maupin",
        "pages": 371
    },
    {
        "title": "Alkeemik",
        "author": "Paulo Coelhe",
        "released": 2014,
        "pages": 182
    },
    {
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J. K. Rowling",
        "released": 1998,
        "pages": 251
    }
]


def authorInitials(authorName):
    # I need to split the author name into seperate parts to show initials
    splitName = authorName.split()
    initials = ""
    # loop through the list of splitted name
    for name in splitName:
        initials += name[0] + ". "

    return initials


def showBooks():
    print("Quick overview of books:")
    for index in range(len(BOOKS)):
        print(str(index + 1) + ". " + BOOKS[index].get("title") +
              " - " + authorInitials(BOOKS[index].get("author")))


def bookInfo(book: Dict):
    """
    Book X by A. B. Bowanga - 1996
    Pages: 222
    Reading time: 13 hours
    """
    readTime = round((float(book.get("pages")) * READ_TIME) / 60.0, 1)
    bookDescription = """
    {} by {} - {}
    Pages: {}
    Reading time: ~{} hours
    """.format(book.get("title"), book.get("author"), 
               book.get("released"), book.get("pages"), str(readTime))
    print(bookDescription)


def showBook():
    bookInfo(BOOKS[chooseBook()])


def chooseBook():
    showBooks()
    choice = int(input("Choose a book: ")) - 1
    return choice


def addBook():
    print("ADD A BOOK")
    newBook = {
        "title": input("Enter book title: "),
        "author": input("Enter book author: "),
        "released": input("Enter release year: "),
        "pages": input("Enter how many pages there are: ")
    }
    print("You have entered a new book!")
    bookInfo(newBook)
    BOOKS.append(newBook)
    # BOOKS.insert(0, newBook) # lisa listi algusesse


def delBook():
    print("DELETE A BOOK")
    chosenBookIndex = chooseBook()
    print("Are You certain you want to remove this book - ", BOOKS[chosenBookIndex].get("title"))
    usersResponse = input("Yes or No")
    if usersResponse == "No":
        exit()
    elif usersResponse == "Yes":
        bookTitle = BOOKS[chosenBookIndex].get("title")
        BOOKS.pop(chosenBookIndex)
        print(bookTitle + " has been deleted.")
        
    # BOOKS.pop(chosenBookIndex) oleks õigem kui delete toimub enne confirmation msg't
    

def startMenu():
    menuOptions = """
    MAIN MENU
1. Show books
2. Choose a book
3. Add a book
4. Del a book

0. Exit
    """
    while True:
        print(menuOptions)
        selection = int(input("Enter your choice: "))
        if(selection == 0):
            exit()
        elif(selection == 1):
            showBooks()
        elif(selection == 2):
            showBook()
        elif(selection == 3):
            addBook()
        elif(selection == 4):
            delBook()
        else:
            print("Couldn't understand your choice, here are the options")


if __name__ == "__main__":
    startMenu()
