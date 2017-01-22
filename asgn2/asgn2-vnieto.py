#guess my number


print("I will guess the number you're thinking of from 1 - max")
minGuess = 1
maxGuess = input("what is the maximum number?: ")
#convert maxGuess to int type since input returns string type
maxGuess = int(maxGuess)
#The guess the computer makes will always be halfway between the current minimum value and the current max
#value
compGuess = int((minGuess + maxGuess) / 2)
userInput = input("Is your number (G)reater, (L)ess, or (E)qual to " + str(compGuess) + "?: ")


while(str(userInput) != 'E'):
    if(str(userInput) == 'G'):
        minGuess = compGuess
        compGuess = int((minGuess + maxGuess)/2)
        userInput = input("Is your number (G)reater, (L)ess, or (E)qual to " + str(compGuess) + "?: ")
    elif(str(userInput) == 'L'):
        maxGuess = compGuess
        compGuess = int((minGuess + maxGuess)/2)
        userInput = input("Is your number (G)reater, (L)ess, or (E)qual to " + str(compGuess) + "?: ")

print("I guessed your number! It was " + str(compGuess) + "!")


