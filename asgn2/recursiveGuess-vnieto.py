#assignment2
#Victor Nieto
#vnieto
def recursiveGuess(min, max):
    #The guess the computer makes will always be halfway between the current minimum value and the current max
    compGuess = int((min + max) / 2)

    userInput = input("Is your number (G)reater, (L)ess, or (E)qual to " + str(compGuess) + "?: ")
    #if compguess is less than users guess, then min becomes computers guess and
    #same function is called recursively with new min and same max
    if(str(userInput) == 'G'):
        min = compGuess
        recursiveGuess(min, max)

    #if compguess is greater than users guess, then max becomes computers guess and
    #same function is called recursively with new max and same min
    elif(str(userInput) == 'L'):
        max = compGuess
        recursiveGuess(min, max)

    #If computers guess is right it prints success statement and returns
    elif(str(userInput) == 'E'):
        print("I guessed your number! It was " + str(compGuess) + "!")
        return



max = input("What is the maximum number?: ")
max = int(max)
recursiveGuess(1, max)

