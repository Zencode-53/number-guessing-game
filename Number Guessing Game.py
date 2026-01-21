import random
import time
print("🎯 Welcome to the Number Guessing game 🎯")
user_name = input("Enter your name: ").title()
user_age = int(input("Enter your age:  "))
time.sleep(0.5)
print()
print("Loading...")
time.sleep(1)
print("Thanks for giving us yor details ✅")
time.sleep(0.5)
print()
print(f"Hey {user_name}! Let's start the game...")
time.sleep(0.5)
print("We have guessed the secret number for you! Now its your turn to guess it...\nYou have 10 attempta left\n(Hint:- The secret number is between 1 to 50)")
time.sleep(1)
print()
Choice = input("Press Enter to start the game---or---Press Q to exit: ").lower()
secret_num = random.randint(1 , 50)
num = 1
attempt = 10
is_guess_correct = False
while num <= 10:
    if Choice == "":
        user_entered_number = int(input("Enter your Guess: "))
        if user_entered_number == secret_num:
            print(f"Hooray🎉🥳...Your guess is correct✅\nYou guessed in {attempt} attempts")
            is_guess_correct = True
            break
        else:
            if user_entered_number < secret_num:
                higher_lower = "Higher"
            else:
                higher_lower = "Lower"

            print(f"Sorry your guess dosen't match😓😭...Please try {higher_lower} number💔! \nYou have only {attempt} Attempts left\n ")
    elif Choice == "q":
        print("Exiting the game...")
        time.sleep(2)
        print("Exited successfully✔....We will miss you!😞😔 See you soon!!🥰💙")
        is_guess_correct = True
        break
    else:
        print("Invalid input❌... Please try again🙂")
        break
    num +=1
    attempt -=1
if is_guess_correct == False:
   print(f"Bad luck!😔💔....\nYour all the attempts are exhausted\nThe secret number was {secret_num}")
print()
print("THANKS FOR CHOOSING US🥰❗")
