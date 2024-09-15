# created date: 12.9.2024
# created by: Tajsia

name = input("Type your name: ")
print(f"Welcome, {name} to this adventure!")

answer = input("You are on the dirt road, it has come to an and."
               "And you can go left or right,"
               "which whay you won to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around or swim across, which way you won to go? ")

    if answer =="swim":
        print("You swim across and you eaten by an alligator.")

    elif answer == "walk":
        print("You walk for many miles, ran out of water an you lost the game.")
    else:
        print("Not vlid option. You lose.")

        #=======================================================
elif answer == 'right':
    answer = input("You come to a bridge, it look wobbly, do you wont to a cross or head back (cross/back)?")

    if answer == "back":
        print("You go back and lose.")

    elif answer == "cross":
        answer = input("You cross the brodge and meat a stranger. do you won to a tolk to him. (no/yes)")

        if answer == "yes":
            print("You talk to a stranger an give you a gold, You WIN!")
        elif answer == "no":
            print("You ignore the stranger, and they are affended and you lose.")
        else:
            print('Not a valid option. You LOSE')

    else:
        print("Not vlid option. You luse.")

else:
    print("Not  valid Option! You lose.")

print('Thank you to trying this game.')

















