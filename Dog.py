import datetime
import Animal

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed # Objekt Attribut

## DRY 
# DON'T REPEAT YOURSELF

## KISS
# Keep it simple stupid 