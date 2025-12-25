from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1. Create the Menu (The list of drinks)
menu = Menu()
# 2. Create the Coffee Maker (The machine with water/milk)
coffee_maker = CoffeeMaker()
# 3. Create the Money Machine (The coin processor)
money_machine = MoneyMachine()

is_on = True

while is_on:
    print(menu.get_items())
    choice = menu.find_drink(input("Choose your drink: ").lower())
    if choice == None: 
        c = int(input("Press 1 to choose again!")) 
        if c == 1:
            continue
        else:
            print("Goodbye!")
            is_on = False
            break
    else:
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)
            else:
                c = int(input("Press 1 to choose again!")) 
                if c == 1:
                    continue
                else:
                    print("Goodbye!")
                    is_on = False
                    break
        else:
            print("Goodbye!")
            is_on = False
        


# print("--- Testing Reports ---")
# coffee_maker.report()
# money_machine.report()

# print("\n--- Testing Menu ---")
# print(menu.get_items())