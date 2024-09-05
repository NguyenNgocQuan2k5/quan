class Mammal:
    def __init__(self, name, type_, sound):
        self.name = name      
        self.type = type_     
        self.sound = sound    
    __kingdom = "animals"
    def make_sound(self):
        return f"{self.name} makes {self.sound}"
    
    def get_kingdom(self):
        return Mammal.__kingdom
    
    def info(self):
        return f"{self.name} is of type {self.type}"

mammal1 = Mammal("Elephant", "herbivore", "trumpet")
print(mammal1.make_sound()) 
print(mammal1.get_kingdom()) 
print(mammal1.info())  