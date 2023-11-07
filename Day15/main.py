#coffee machine program
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_check(ingredients):
    """Returns false if there are not enough resources, else returns true"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print (f"Sorry there is not enough {item}")
            return False
    return True


def payment():
    """Returns the total calculated from coins inserted by customer"""
    print ("Please insert coins:")
    total = int (input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.1
    return total


def transaction(money_received, drink_cost):
    """Return True if the payment is accepted or false if the money not enough"""
    if money_received >= drink_cost:
        change = round (money_received - drink_cost,2)
        print (f" Here is your change {change}")
        global profit
        profit +=drink_cost
        return True
    else:
        print ("Sorry, not enough money !")
        return False


def make_coffe (drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]



ok = True
while ok:
    choice= input ("What would you like? (espresso/latte/cappucciono): ")
    if choice == 'off':
        print ("Goodbay !")
        ok = False
    elif choice == 'report':
        print(f"water: {resources['water']}"),
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print (f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resource_check(drink['ingredients']):
            pay = payment()
            if transaction(pay, drink["cost"]):
                make_coffe(choice, drink['ingredients'])




