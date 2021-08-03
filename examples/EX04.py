"""
 Create a book class, which includes the following variables - "Title", "Author", "Publishing date", "Rating", "Pages".
 Class should have a couple of methods aswell.
 1) print "title"
 2) print "info"
 3) rating method
 4) editing method
"""

"""
 tips n tricks - alusta klassi tegemisest, kus on kõik palutud väljad ning default väärtused.
 proovi klassist neid väärtuseid välja printida.
 kui << on tehtud siis proovi teha INIT kust võetakse kõik väärtused peale ratingu
 kui väärtused peale ratingu on omistatud, siis pärast seda proovi teha nt esimene meetod sinna sisse
"""


class Book():
    title = " no name "
    author = " no name "
    publishDate = " not published"
    pages = " no pages "
    rating = "0 / 10"

    READ_TIME = 1.7

    def __init__(self, title, author, publishDate, pages):
        self.title = title
        self.author = author
        self.publishDate = publishDate
        self.pages = pages

    def printTitle(self):
        print(self.title)

    def printAuthor(self):
        print(self.author)

    def printPublishDate(self):
        print(self.publishDate)

    def printPages(self):
        print(self.pages)

    def authorInitials(self):
        splitName = self.author.split()
        initials = ""

        for name in splitName:
            initials += name[0] + ". "

        return initials

    def printInfo(self):
        readTime= round(((float(self.pages)) * self.READ_TIME) / 60.0, 1)
        bookInfo= """
        {} by {} - {}
        Pages: {}
        Reading time: ~{} hours
        Rating: {}
        """.format(self.title, self.authorInitials(), self.publishDate, self.pages, readTime, self.rating)

        print(bookInfo)

    def rate(self, rating):
        self.rating = "{} / 10".format(str(rating))

    def editInfo(self, field, value):
        if field == "title":
            self.title = str(value)
        
        elif field == "author":
            self.author = str(value)
        
        elif field == "released":
            self.publishDate = int(value)
        
        elif field == "pages":
            self.pages = int(value)

        elif field == "rating":
            self.rate(value)
        



raamat1= Book("Learning .py with Rass", "Rasmus Koit", 2021, 333)
print(raamat1.title)
print(raamat1.author)
print(raamat1.publishDate)
print(raamat1.pages)

raamat1.printInfo()
raamat1.rate(5)
raamat1.printInfo()
raamat1.editInfo("title", "I learn't nothing today")
raamat1.printInfo()

