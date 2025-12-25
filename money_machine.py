class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: ${self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        self.money_received = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:           
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
            