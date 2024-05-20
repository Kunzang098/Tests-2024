import random
secret_number = random.randint(1,10)
max_attempts = 3

def welcome_message():
    print("\nWelcome to the Number Guessing Game!")
    print(f"You havw {max_attempts} attempts to guess the correct number.")

def guess_recursive(attempt_left):
    guess = int(input("\n Guess th enumber (between 1 to 10):"))

    if guess ==secret_number:
      print("Congratulation! You Guessed the correct number")
    else:
       print(F"Wrong guess,attempt left: {attempt_left-1}")
       if attempt_left > 1:
          guess_recursive(attempt_left-1)
       else:
          print(f"\n Sorry, you couldn't guess the number. The correct number was {secret_number}.")  

    welcome_message()
    guess_recursive(max_attempts) 
    print(f"Memory adress of Secret Number {secret_number} is: {id(secret_number)}")



        

