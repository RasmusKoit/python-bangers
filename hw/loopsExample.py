listOfBookDictionaries = [{"title": "Aabits"}, {"title": "Hulkur Rasmus"}, {"title": "Harry Potter"}]


index = 0
lastIndex = len(listOfBookDictionaries)
while(index < lastIndex): 
    book = listOfBookDictionaries[index]
    title = book.get("title")
    print(title)
    index += 1 # index = index + 1
    

for index in range(0, lastIndex):
    book = listOfBookDictionaries[index]
    title = book.get("title")
    print(title)
    
for book in listOfBookDictionaries:
    title = book.get("title")
    print(title)
    
for book in listOfBookDictionaries:
    print(book.get("title"))
    
listOfBooks = [{"title": "Aabits"}, {"title": "Hulkur Rasmus"}, {"title": "Harry Potter"}]
listOfRecipes = [{"title": "Makaronid hakklihaga"}, {"title": "Pannkoogid"}]
listOfFilms = [{"title": "FF9"}, {"title": "FF: Tokyo Drift"}]

def showTitle(inputList):
    for element in inputList:
        print(element.get("title"))
        
showTitle(listOfBooks)
showTitle(listOfRecipes)
showTitle(listOfFilms)