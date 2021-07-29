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

def authorInitials(authorName):
    # I need to split the author name into seperate parts to show initials
    splitName = authorName.split()  
    initials = ""
    # loop through the list of splitted name
    for name in splitName:
        initials += name[0] + ". "

    return initials

if __name__ == "__main__":
    print(authorInitials("Rasmus Koit"))

