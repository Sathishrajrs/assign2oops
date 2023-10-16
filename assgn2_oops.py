class dog:
    def __init__(self):
        self.name=input("Enter Dog Name:")
        self.age=int(input("Enter Dog Age:"))
        self.coat=input("Enter Dog Coat Color:")

    def description(self):
        print("Dog Name:",self.name)
        print("Dog Age:",self.age)

    def get_coat(self):
        return self.coat
    
class JackRussellTerrier(dog):
    def breed(self):
        self.home=input("Enter Foreign or Native Breed:")
        print("Breed:",self.home)

    def sexMorF(self):
        self.sex=input("Enter sex Male Or Female:")
        print("Breed:",self.sex)

class Bulldog(JackRussellTerrier):
    def uses(self):
        self.activity=input("Enter Usecase:")
        print("Usecase:",self.activity)

    def character(self):
        self.char=input("Enter Mode Of Character:")
        print("Mode of Character:",self.char)

obj=Bulldog()
obj.description()
print("Dog Coat colour:",obj.get_coat())
obj.breed()
obj.sexMorF()
obj.uses()
obj.character()




