MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 15,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 20,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO : 1 print the report of coffe machine

# TODO : 2 check the resources sufficient to make drink.

def is_resources_efficient(order_ingredients):
    """ Return the true when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    """ Return total calculated from coins inserted."""
    print("please insert the coin")
    total = int(input("how many one rupee coins? :")) * 1
    total += int(input("how many Two rupee coins? :")) * 2
    total += int(input("how many Five rupee coins? :")) * 5
    total += int(input("how many Ten rupee coins? :")) * 10
    return total


def transaction_successful(money_received, drink_cost):
    """return true when payment is successful is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change}RS in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"sorry that's not enough money. {money_received}rs money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    """deducts the  required ingredients  from the resources"""
    global  resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f" here is your {drink_name}.")


power = True

while power:
    choice = input(" What would you like? (espresso RS 10/latte RS 15 /cappuccino RS 25): ")
    if choice == "off":
        power = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['water']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        drink_cost = MENU[choice]['cost']
        if is_resources_efficient(drink['ingredients']):
            payment = process_coin()
            if transaction_successful(payment, drink_cost):
                make_coffe(choice, drink["ingredients"])
