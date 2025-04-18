# main.py
from pet import Pet

def main():
    # Create a pet
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    print(f"\nWelcome, {my_pet.name}! Let's take care of your new pet.")
    
    while True:
        print("\nOptions:")
        print("1. Feed your pet")
        print("2. Put your pet to sleep")
        print("3. Play with your pet")
        print("4. Check pet status")
        print("5. Teach your pet a trick (Bonus)")
        print("6. Show learned tricks (Bonus)")
        print("7. Quit")
        
        choice = input("What would you like to do? (1-7): ")
        
        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            my_pet.get_status()
        elif choice == "5":
            trick = input("What trick would you like to teach? ")
            my_pet.train(trick)
        elif choice == "6":
            my_pet.show_tricks()
        elif choice == "7":
            print(f"Goodbye! Take care of {my_pet.name}!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()