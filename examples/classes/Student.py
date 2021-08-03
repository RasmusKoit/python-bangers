from Person import Person

class Student(Person):
  def __init__(self, fname, lname, startYear):
    super().__init__(fname, lname)
    self.startYear = startYear

isik = Student("Rasmus", 25, 2015)
isik.printName()


