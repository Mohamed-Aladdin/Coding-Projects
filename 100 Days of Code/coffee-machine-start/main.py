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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def get_order(ordr):
    return MENU[ordr]

def get_report():
    return resources["water"], resources["milk"], resources["coffee"], resources["money"]

def check_resources(ordr, req):
    y = 0.1
    x = resources["water"] - ordr["ingredients"]["water"]
    z = resources["coffee"] - ordr["ingredients"]["coffee"]
    if req != "espresso":
        y = resources["milk"] - ordr["ingredients"]["milk"]
    return x < 0 or y < 0 or z < 0

def calcualte_resources(ordr, cost, req):
    resources["water"] -= ordr["ingredients"]["water"]
    resources["coffee"] -= ordr["ingredients"]["coffee"]
    resources["money"] += cost
    if req != "espresso":
        resources["milk"] -= ordr["ingredients"]["milk"]

def get_price(ordr):
    cost = ordr["cost"]
    return cost

def get_payment(cost):
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))
    payment = (q*25 + d*10 + n*5 + p) / 100
    change = payment - cost
    change = round(change, 2)
    return payment, change

def check_payment(payment, cost):
    if payment > cost:
        return False
    return True

def main():
    terminate = False
    while not terminate:
        request = input("What would you like to order? (espresso/latte/cappuccino): ").lower()
        if request == "off":
            print("Shutting down. Bye Bye!")
            break
        elif request == "report":
            water, milk, coffee, money = get_report()
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${money}")
            continue
        elif request not in ("espresso", "latte", "cappuccino"):
            print("Please choose a valid drink!")
            continue
        order = get_order(request)
        out_of_stock = check_resources(order, request)
        if out_of_stock:
            print("There's not enough resources!")
            continue
        cost = get_price(order)
        print("Please insert payment!")
        payment, change = get_payment(cost)
        not_enough = check_payment(payment, cost)
        if not_enough:
            print("Sorry, that's not enough money! Money refunded.")
            break
        print(f"Here's ${change} in change!")
        print(f"Here's is your {request}. Enjoy!")
        calcualte_resources(order, cost, request)

main()