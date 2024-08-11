class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.menu = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
        }
        self.money = 0.0

    def is_resource_sufficient(self, drink):
        """Check if there are enough resources to make the drink."""
        for item in self.menu[drink]:
            if item != "cost" and self.menu[drink][item] > self.resources[item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Process coins and return the total amount inserted."""
        print("Please insert coins.")
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.10
        total += int(input("How many nickels?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
        return total

    def make_coffee(self, drink):
        """Deduct the required resources and make the coffee."""
        for item in self.menu[drink]:
            if item != "cost":
                self.resources[item] -= self.menu[drink][item]
        print(f"Here is your {drink} ☕️. Enjoy!")

    def report(self):
        """Print the current resource status."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money}")

    def start(self):
        """Start the coffee machine."""
        is_on = True

        while is_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                is_on = False
            elif choice == "report":
                self.report()
            elif choice in self.menu:
                if self.is_resource_sufficient(choice):
                    payment = self.process_coins()
                    if payment >= self.menu[choice]["cost"]:
                        change = round(payment - self.menu[choice]["cost"], 2)
                        print(f"Here is ${change} in change.")
                        self.money += self.menu[choice]["cost"]
                        self.make_coffee(choice)
                    else:
                        print("Sorry, that's not enough money. Money refunded.")
            else:
                print("Invalid choice. Please select a valid option.")


# Initialize and start the coffee machine
coffee_machine = CoffeeMachine()
coffee_machine.start()
