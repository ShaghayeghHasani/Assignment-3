import random

pc_number = random.randint(0,20)
ug = 0

while True:
    user_number = int(input("Guess a number between 0 and 20:"))
    
    ug += 1

    if pc_number == user_number:
        print("Well done! Number of your guesses is :", ug)
        break

    if user_number < pc_number :
        print ("higher!")
    else:
        print ("lower!")