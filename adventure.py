name = input("Enter Your Name: ")
print("Welcome",name,"to this adventure")

answer = input("You are on a dirt road ,it has come to an end and you can choose to go left or right.Which way would you like to go ? ").lower()

if answer == "left":
    q2 = input("You have come to a river.You can walk across it or swim accross? type 'walk' to walk around it and 'swim' to swim across it: ")
    if q2 == "walk":
        print("You walked for many miles,ran out of water and lost the game!")
    elif q2 == "swim":
        print("You swam across and were eaten by an alligator.")
    else:
        print("Not a valid option.You lose!")

elif answer == "right":
   q2 = input("You come to a bridge ,it looks wobbly ,do you like to cross it or go back? (cross/back)")
   if q2 == "back":
        print("You go back you lose!")
   elif q2 == "cross":
        answer = input("You cross the bridge and talk to a stranger.Dou talk to them?(yes/no)").lower()
        if answer == "yes":
            print("You talk to the stranger the give you gold. You win!")

        elif answer == "no":
             print("You ignore the stranger they get offended. You lose!")
        else:
             print("Not a valid option.You lose!")
   else:
        print("Not a valid option.You lose!")

else:
    print("Not a valid option.You lose!")