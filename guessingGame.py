secretWord = "giraffe"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuesses = False

while guess != secretWord and not(outOfGuesses):
    if guessCount < guessLimit:
        guess = input("Enter guess: ")
        guessCount += 1
    else:
        outOfGuesses = True

if outOfGuesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("YOU WIN!")