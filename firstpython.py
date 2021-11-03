numberGuess=int(input(" Enter your guess number between 1-9"))
if(numberGuess>10):
    print("You Loose")
if not numberGuess >7:
    print("You entered small number")
elif(numberGuess <2):
    print("You entered large number")
else:
    print("You Won")
