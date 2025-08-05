

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
}
r_water=resources['water']
r_milk=resources['milk']
r_coffee=resources['coffee']
espress_water=(MENU["espresso"]['ingredients']['water'])
espress_coffee=(MENU["espresso"]['ingredients']['coffee'])
latte_water=(MENU["latte"]['ingredients']['water'])
latte_milk=(MENU["latte"]['ingredients']['milk'])
latte_coffee=(MENU["latte"]['ingredients']['coffee'])
cappucc_water=(MENU["cappuccino"]['ingredients']['water'])
cappucc_milk=(MENU["cappuccino"]['ingredients']['milk'])
cappucc_coffee=(MENU["cappuccino"]['ingredients']['coffee'])
money=0
game=True
while game:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=='off':
        game=False
    elif choice=='report':
        print(f"water: {r_water},milk: {r_milk},coffee: {r_coffee},money: ${money}")
    elif choice == 'espresso':
        if r_water < espress_water:
            print('out of resources')
        elif r_coffee < espress_coffee:
            print('out of resources')
        elif r_water>espress_water and r_coffee>espress_coffee:
            print('Please insert coins.')
            quarters = int(input('How many quarters?: ')) * 0.25
            dimes = int(input('how many dimes?: ')) * 0.10
            nickles = int(input('how many nickles?: ')) * 0.05
            penny = int(input('how many pennies?:')) * 0.01
            total = quarters + dimes + nickles + penny
            if total < 1.5:
                print('Not enough money')
            else:
                r_water = r_water - espress_water
                r_coffee = r_coffee - espress_coffee
                change = round(total - 1.5,2)
                money+=1.5
                print(f'Here is ${change} in change.')
                print("Here is your espresso ☕️. Enjoy!")

    elif choice == 'latte':
        if r_water < latte_water:
            print('out of resources')
        elif r_milk < latte_milk:
            print('out of resources')
        elif r_coffee < latte_coffee:
            print('out of resources')
        elif r_water>latte_water and r_milk>latte_milk and r_coffee>latte_coffee:
            print('Please insert coins.')
            quarters = int(input('How many quarters?: ')) * 0.25
            dimes = int(input('how many dimes?: ')) * 0.10
            nickles = int(input('how many nickles?: ')) * 0.05
            penny = int(input('how many pennies?:')) * 0.01
            total = quarters + dimes + nickles + penny
            if total < 2.5:
                print('Not enough money')
            else:
                r_water = r_water - latte_water
                r_milk = r_milk - latte_milk
                r_coffee = r_coffee - latte_coffee
                change = round(total - 2.5,2)
                money+=2.5
                print(f'Here is ${change} in change.')
                print("Here is your latte ☕️. Enjoy!")

    elif choice == 'cappuccino':
        if r_water < cappucc_water:
            print('out of resources')
        elif r_milk < cappucc_milk:
            print('out of resources')
        elif r_coffee < cappucc_coffee:
            print('out of resources')
        elif r_water>cappucc_water and r_milk>cappucc_milk and r_coffee>cappucc_coffee:
            print('Please insert coins.')
            quarters = int(input('How many quarters?: ')) * 0.25
            dimes = int(input('how many dimes?: ')) * 0.10
            nickles = int(input('how many nickles?: ')) * 0.05
            penny = int(input('how many pennies?:')) * 0.01
            total = quarters + dimes + nickles + penny
            if total < 3.0:
                print('Not enough money')
            else:
                r_water = r_water - cappucc_water
                r_milk = r_milk - cappucc_milk
                r_coffee = r_coffee - cappucc_coffee
                change = round(total - 3.0,2)
                money+=3.0
                print(f'Here is ${change} in change.')
                print("Here is your cappuccino ☕️. Enjoy!")
    else:
        print('wrong input')






