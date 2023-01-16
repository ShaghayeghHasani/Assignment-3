import random

while True:
    Dice = random.randint(1,6)
    User = str(input("Do you want to roll the dice?(yes/no):"))
    if User == "yes":
        print (Dice)
        if Dice == 6:
            confirmation = input("You get two more dice rolls. Press Enter to get your bonus.")
            if confirmation == "" :
                for i in range (2):
                    Bonus = random.randint(1,6)
                    print (Bonus)
        else:
            print("Roll again.")
    if User == "no" :
        break