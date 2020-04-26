
print("Try to Guess, Daniel´s favorite fruit ")

secret_word = "Lemon"
guess = ""

while guess != secret_word :
    guess = input("Enter the guess: ")
    if guess != secret_word :
        print("Try again.")
    else:
        print("You win")