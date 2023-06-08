from data import MENU, resources


off = False

money = 0

def check_resources(coffee):
    coffee_obj = MENU[coffee]['ingredients'] #return the dict ingredients dict
    for key in coffee_obj:
        if coffee_obj[key] <= resources[key]:
            resources[key] = resources[key] - coffee_obj[key]
            
        else:
            print(f"sorry not enough {key}")
            return False
    return True


def insert_coins():
    quarter = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickel = int(input("how many nickels: "))
    pennies = int(input("how many pennies: "))
    coins ={
        "quarter": quarter,
        "dimes": dimes,
        "nickel": nickel,
        "pennies": pennies
    }

    total = coins['quarter']*0.25 + coins['dimes']*0.1 + coins['nickel']*0.05 + coins['pennies']*0.01
    return total



def process_money(coins_inserted, coffee):
    global money
    change = coins_inserted - MENU[coffee]['cost']
    money = money + MENU[coffee]['cost']
    return round(change, 2)



def check_coins(coins_inserted, coffee):
    if MENU[coffee]['cost'] <= coins_inserted:
        enough_money = True
        user_change = process_money(coins_inserted, coffee)
        print(f"here is your change: ${user_change}")
        
    else:
        enough_money = False
        print("you have not inserted enough money")
    return enough_money



while not off:
    coffee = input("what kind of coffee? 'Latte', 'Cappuccino', or 'Espresso'?: ").lower()
    if coffee == "off":
        off = True
    elif coffee == "report":
        print(f"milk: {resources['milk']}")
        print(f"water: {resources['water']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: {money}")

    elif check_resources(coffee):
        # insert_coin
        coins_inserted = insert_coins()
        if check_coins(coins_inserted, coffee):
            print(f"Here is your coffee: {coffee}... enjoy")
        
    




