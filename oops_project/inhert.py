class Animal:
    def __init__(self, name):
        self.name=name
        print('Animal is calllled')
    
    def eat(self):
        print(f'{self.name} is animal eating')

#Animal attributes gets inherited 
class Dog(Animal):

    def __init__(self):
        super().__init__('Foggy')
    def bark(self):
        print(f'{self.name} is barking')
    
    def eat(self):
        super().eat()
        print(f'{self.name} doggy is eating')

dog=Dog()
dog.eat()
dog.bark()
    



        
    
