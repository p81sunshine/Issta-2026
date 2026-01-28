class AnimalShelterGame:
    def __init__(self):
        self.balance = 100
        self.adopted_animals = []

    def adopt(self, animal):
        adoption_fees = {"cat": 20, "dog": 50, "fish": 10}
        if animal not in adoption_fees:
            return "Invalid animal choice."
        fee = adoption_fees[animal]
        if self.balance >= fee:
            self.balance -= fee
            self.adopted_animals.append(animal.capitalize())
            return f"You have adopted a {animal}."
        else:
            return "You don't have enough money to adopt this animal."

    def view_balance_and_adopted_animals(self):
        return {"balance": self.balance, "adopted_animals": self.adopted_animals}

    def quit_game(self):
        return "Game Over. Thank you for playing!"

    def play(self):
        print("Welcome to the Animal Shelter!")
        while self.balance > 0:
            print(f"\nYou have ${self.balance:.2f}")
            print(f"You have adopted: {self.adopted_animals}")
            print("What would you like to do?")
            print("1. Adopt a cat ($20)")
            print("2. Adopt a dog ($50)")
            print("3. Adopt a fish ($10)")
            print("4. View balance and adopted animals")
            print("5. Quit")

            choice = input("\nChoose a numbered option: ")
            if choice == '1':
                print(self.adopt("cat"))
            elif choice == '2':
                print(self.adopt("dog"))
            elif choice == '3':
                print(self.adopt("fish"))
            elif choice == '4':
                balance_info = self.view_balance_and_adopted_animals()
                print(f"\nBalance: ${balance_info['balance']:.2f}")
                print(f"Adopted animals: {balance_info['adopted_animals']}")
            elif choice == '5':
                print(self.quit_game())
                break
            else:
                print("Invalid input, please select a valid option.")

            if self.balance <= 0:
                break