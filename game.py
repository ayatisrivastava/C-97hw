number=7
print("Number Guessing Game")
print("Guess the Number (between 1-9)")
input("Enter you guess:- ")
chances=5
if(number<7):
    while chances<5:
        print("Oops! Guess your number is a little low...")
elif(number>7):
    print("Uh-uh, your guess is a little too high.")
else:
    print("CONGRATULATIONS! YOU GUESSED THE CORRECT NUMBER! YOU WON!")
