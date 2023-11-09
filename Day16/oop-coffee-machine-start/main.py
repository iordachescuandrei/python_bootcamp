from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
maker = CoffeeMaker()
machine = MoneyMachine()



ok = True
while ok:
    user_choice = input("What would you like?  espresspo / latte / cappuccino: ")
    client = menu.find_drink(user_choice)
    if user_choice == 'report':
        maker.report()
        machine.report()
        exit()
    else:
        if client != None:
            if maker.is_resource_sufficient(client) and  machine.make_payment(client.cost):
                maker.make_coffee(client)
            else:
                ok=False
        else:
            ok=False

