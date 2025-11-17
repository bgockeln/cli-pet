# My first attempt at OOP.

# The Pet object: Creating my Pet with a name attribute that can be changed
# and other attributes that already have a set value.
import os
import sys
import platform
from pet import Pet

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Main Loop
def main():
    pet_name = input("Name your pet: ")
    my_pet = Pet(pet_name)

    while True:
        clear_screen()
        my_pet.watch_pet()
        print("\n--- Pet Menu ---")
        print("1. Play")
        print("2. Give Food")
        print("3. Give Water")
        print("4. Show Status")
        print("5. Quit")

        choice = input("Choose an action: ")

        if choice == "1":
            print(f"Mood Level:", my_pet.mood)
            my_pet.play()
            print(f"New mood level after playing:", my_pet.mood)
            input("Press Any Key")
        elif choice == "2":
            print("Hunger Level:", my_pet.hunger)
            my_pet.eat()
            print("New hunger level after eating:", my_pet.hunger)
            input("Press Any Key")
        elif choice == "3":
            print("Thirst Level", my_pet.thirst)
            my_pet.drink()
            print("New thirst level after drinking:", my_pet.thirst)
            input("Press Any Key")
        elif choice == "4":
            my_pet.status()
            input("Press Any Key")
        elif choice == "5":
            print("Doeiiiii!")
            input("Press Any Key To Exit")
            sys.exit(0)
        else: 
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()