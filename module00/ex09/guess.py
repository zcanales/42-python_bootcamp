import random

# rand = 42

def guess():
    print("This is an interactive guessing game!\nYou have to",
      "enter a number between 1 and 99 to find out the secret number.",
      "\nType 'exit' to end the game.\nGood luck!\n")
    rand = random.randint(1, 99)
    attempt = 0
    while (1):
        try:
            choice = input("What's your guess between 1 and 99?\n>> ")
            if (choice == "exit"):
                return
            integer = int(choice)
            if (integer == rand):
                if integer == 42:
                    print("The answer to the ultimate question of life,","the universe and everything is 42.")
                elif attempt == 1:
                     print("Congratulations! You got it on your first try!")
                else:
                     print("Congratulations, you've got it!",
                      f"""\nYou won in {attempt} attempts!""")
                return
            if (integer > rand):
                print("Too high!")
            else:
                print("Too low!")
            attempt += 1
        except ValueError:
            print("Not Number")


      

guess()
