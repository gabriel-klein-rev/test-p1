# CLI application that keeps a record of animals I own
# Animal types: Animal, Cat, Dog
#           - Attributes: Name, Age
# Want to store our animal information to a file
# Upon restarting application, want to load animal data from file

# Importing animal module
import animal
import re

# Used to create animal object from user-inputted values
def add_animal() -> animal.Animal:
    # Input verification
    while True:
        try:
            print("Hello! Please select type of animal to input:")
            print("\t a) Generic animal")
            print("\t c) Cat")
            print("\t d) Dog")
            typeAnimal = input(">>>")

            
            if not typeAnimal == 'c' and not typeAnimal == 'd' and not typeAnimal == 'a':
                raise ValueError('Invalid input for animal type')
            else:
                break
        except ValueError:
            print("Oh no! Please enter a valid type for animal! ('a', 'c', 'd')")
            pass

    while True:
        try:
            print("\n\nEnter animal name:")
            name = input(">>>")
            if not re.search(r"[,\.\\\*\-]", name) == None:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please do not use special characters in your name for your animal!")


    while True:
        try:
            print("\n\nEnter animal age:")
            age = int(input(">>>"))
            break
        except ValueError:
            print("Oh no! You must enter a number for the age! Try again!")

    if typeAnimal == 'a':
        newAnimal = animal.Animal(name, age)
    elif typeAnimal == 'c':
        newAnimal = animal.Cat(name, age)
    else:
        newAnimal = animal.Dog(name, age)
    
    return newAnimal


# Save animal list to saved_animals.txt
def save_animals(lst_Animals):
    f = open('saved_animals.txt', 'w')

    for animal in lst_Animals:
        f.write(animal.name + ',' + str(animal.age) + ',' +  animal.animal_type + "\n")

    f.close()

# Load animals from saved_animals.txt
def load_animals():
    f = open('saved_animals.txt', 'r')
    lst_animals = []
    for line in f:
        if line == '':
            break

        animal_data = line.split(',')
        if animal_data[2].strip() == 'Generic':
            newAnimal = animal.Animal(animal_data[0], animal_data[1])
        elif animal_data[2].strip() == 'Cat':
            newAnimal = animal.Cat(animal_data[0], animal_data[1])
        else:
            newAnimal = animal.Dog(animal_data[0], animal_data[1])
        
        lst_animals.append(newAnimal)
    f.close()
    return lst_animals

#Main function
def main():
    print("Welcome to the Animal Journal")

    lst_Animals = load_animals()
    while True:
        try:
            print("Please select an option:")
            print("\ta) Add new Animal")
            print("\tq) Quit")

            option = input(">>>")

            if option == 'q':
                break
            elif option == 'a':
                lst_Animals.append(add_animal())
            else:
                raise ValueError('Invalid menu option')
        except ValueError as ve:
            print(ve)
            print("Invalid option! Please try again!")
    
    for animal in lst_Animals:
        print(animal, type(animal))
    
    save_animals(lst_Animals)


if __name__ == '__main__':
    main()





