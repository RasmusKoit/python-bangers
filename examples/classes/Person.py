class Person():

    def __init__(self, name, age):
            self.name = name
            self.age = age
            
    def printName(self):
        print("This person is called", self.name, "and he is", self.age)

class Child(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        
laps = Child("Madi", 12, "Kohila Gymnaasium")

print(laps.school)