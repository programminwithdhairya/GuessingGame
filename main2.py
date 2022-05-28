# Guessing game in Python 
import random 
randnum  = random.randint(1,100)
# print(randnum)
print("You will get only 5 Chances to Guess the number")

def Guess():
    guesses = 1
    while True:
        user_guess = int(input("Enter Your Guess:\n"))
        if user_guess == randnum:
            print(f"you won!! , You took {guesses} gusses")
            exit()
            
        else:
            if user_guess > randnum : 
                print("You are guessing a big number guess a Small number")
                guesses  = guesses + 1

            else:
                print("You are guessing a small number Guess a big number")
                guesses  = guesses + 1
        if guesses == 5:
                print(f"Game Over.... you took {guesses} Guesses")
                break


game = Guess()
print(game)
