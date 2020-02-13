
import random

words = ['digger','snake','laboratory','absurd','azure','circuit','oxygen'] #Add as many words as you want
numWords = len(words)
chooseIndex = random.randint(1,numWords-1)
chosen = words[chooseIndex]                #chooses a random word
startSet = '_ '*len(chosen)     #Creates placeholders for each letter in the word
print("Your word:",startSet)
numTry = len(chosen)*2    #Can be set to however many tries you want to give the player
correctRep = 0            #Create counter for correctly guessed letters

def Guess(chosen,startSet,numTry,correctRep):     #function to run for the player guessing a letter
    guess = input('Guess a letter: ')
    if len(guess) == 1 & guess.isalpha() == True: #checks that user input is a single letter
        if guess in chosen:                        #checks if guessed letter is in the word
            for i in range(len(chosen)):
                if guess in chosen[i]:                 #for each instance of the guessed letter in the word,
                    startSet = startSet[:i*2] + guess + startSet[i*2+1:] #Replace a _ with the letter
                    correctRep = correctRep+1                            #Increase correct score
                    chosen = chosen[:i]+'1'+chosen[i+1:]                 #Replace the guessed letter with 1 so it...
        else:                                                            #...cannot be guessed again
            print("Wrong Guess")
            numTry = numTry-1                    #Subtract a try for a wrong guess
    else:
        print("Idiot")
        numTry = numTry-1                   #Insult player and subtract a try if a non single letter is guessed
    return(startSet,correctRep,numTry,chosen)  #extract needed info for next loop

while numTry > 0:     #Runs until the player is out of tries
    (startSet,correctRep,numTry,chosen) = Guess(chosen,startSet,numTry,correctRep) #Runs guess code
    print("Tries left: ",numTry)            #info to player
    print(startSet)                         #Current progress to player
    if correctRep >= len(chosen):           #When all letters are guessed disp win message and stop the loop
        print("You Won")
        break
    elif numTry == 0:                       #When all tries are used, disp failure message and the loop will terminate
        print("Game Over")



