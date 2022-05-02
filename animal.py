# Parent class
class Animal:
    isAlive = True
    animal_type = 'Generic'

    # Cunstructor/initializer of object
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = 'Generic'

    def sleep(self):
        print('*zzz*')
        return "*zzz*"

    def move(self):
        print(self.name, "has moved.")
        return self.name + " has moved."

    def eat(self):
        print(self.name, "has gained energy.")
        return self.name + " has gained energy."

    def __str__(self):
        return self.name + ": " + str(self.age)

    def death(self):
        print(self.name, "has died.")
        self.isAlive = False
        
# Child class of Animal
class Cat(Animal):
    animal_type = 'Cat'
    def sleep(self):
        print("*purr*")
        return("*purr*")

    def move(self):
        print(self.name, "has walked.")
        return self.name + " has walked."
# Child class of Animal
class Dog(Animal):
    animal_type = 'Dog'
    def sleep(self):
        print("*snore*")
        return("*snore*")

    def move(self):
        print(self.name, "has run.")
        return self.name + " has run."

    


# Initializing instances of Animal/Cat/Dog

def main():
    a1 = Animal("Fred", 5)
    c1 = Cat("Bob", 4)
    d1 = Dog("Fido", 2)

    lst_animals = [a1, c1, d1]

    for obj in lst_animals:
        print(obj)
        obj.sleep()
        obj.move()
        obj.eat()

if __name__ == '__main__':
    main()
