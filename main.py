import dict
import os


def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')


def resource_check(drink_ordered):
    '''
    This function is checking that the machine has enough resources to make the order. It loops through drinks ingredients to grab the correct ingredients. Then it compares the values between what the machine has and what the recipe calls for. If all pass then it will return the cost to use later. Else, it will reprompt you.
    '''
    count = 0
    for ingredient in dict.MENU[drink_ordered]['ingredients']:
        if dict.MENU[drink_ordered]['ingredients'][ingredient] <= dict.resources[ingredient]:
            count += 1
        else:
            print(f"Not enough {ingredient}.")
            input()
            clrscr()
            continue
        if count == len(dict.MENU[drink_ordered]['ingredients']):
            return True
                

def transaction(payment_needed):
    '''
    The input is the cost of the coffee requested. The function determines how the transaction of money goes.
    '''
    awaiting_payment = True
    while awaiting_payment == True:
        quarters = int(input("Quarters to pay with: "))*0.25
        dimes = int(input("Dimes to pay with: "))*0.10
        nickels = int(input("Nickels to pay with: "))*0.05
        pennies = int(input("Pennies to pay with: "))*0.01

        paid = quarters + dimes + nickels + pennies

        if paid >= payment_needed:
            if paid > payment_needed:
                change = paid - payment_needed
                print(f"Here is your change back: ${change}")
                earned = paid - change
                awaiting_payment = False
            else:
                earned = paid
                awaiting_payment = False
        else:
            print("Sorry that is not enough")
    return earned   


def resources_used(drink_made):
    '''
    Input is the order. Updates resources available in the machine.
    '''
    for ingredient in dict.MENU[drink_made]['ingredients']:
        dict.resources[ingredient] -= dict.MENU[drink_made]['ingredients'][ingredient]


def cost_check(drink_ordered):
    '''
    Input is the order. Grabs cost of the order.
    '''
    cost = dict.MENU[drink_ordered]['cost']
    return cost


machine_on = True
money = 0.00

while machine_on == True:
    order = input("What would you like to order for a coffee? Espresso, latte, or cappuccino?").strip().lower()

    if order == "off":
        machine_on = False
        break
        input()
    
    # Gives report on resources available in machine.
    elif order == 'report':
        print(f"Water: {dict.resources['water']}ml")
        print(f"Milk: {dict.resources['milk']}ml")
        print(f"Coffee: {dict.resources['coffee']}g")
        print(f"${money}")
        continue

    else:
        has_resources = resource_check(drink_ordered = order)

    # resource_check returns the cost of the drink.
    if has_resources == True:
        drink_cost = cost_check(drink_ordered = order)
        print(f"The {order} will cost ${drink_cost}0.")

        money += transaction(payment_needed = drink_cost)

        resources_used(drink_made = order)

        print(f"Here is your {order}.")



    