import math, random 

#Here I set all my variables 
userChoice = ''
computerChoice = ''
answer = ''
currentUserScore = 0
currentComputerScore = 0
totalUserScore = 0 
totalComputerScore = 0

print('Welcome to the coin flip game. You will play against a computer to see who has the best luck!')

def beginGame():
    #Here I set my global variables so that I can modify them in the function
    global userChoice
    global answer
    global computerChoice

    print('Would you like to be Heads or Tails?')
    userDecision = str(input())

    #I use if, else if and else statements to determine what the user and computer plays as.
    if userDecision.upper() == 'HEADS':
        userChoice = 'Heads'
        computerChoice = 'Tails'
    elif userDecision.upper() == 'TAILS':
        userChoice = 'Tails'
        computerChoice = 'Heads'
    else:
        print('Please state whether you want to be heads or tails')
        beginGame()

    print('You have selected ' + userChoice + ', so the computer will be ' + computerChoice + '.')

    #Here I set a random integer to be picked; either 0 or 1.
    randomNumber = random.randint(0, 1)

    #This if, else if statement determines what the answer is depending on the value of randomNumber and calls the next function the work out the score.
    if randomNumber == 0:
        print('It\'s heads!')
        answer = 'Heads'
        resultScore()
    elif randomNumber == 1:
        print('It\'s tails!')
        answer = 'Tails'
        resultScore()

def resultScore():
    global currentComputerScore
    global totalComputerScore
    global currentUserScore
    global totalUserScore
    global userChoice
    global answer
    global computerChoice

    #Here I set the current user/computer scores to 0 so that for each new turn a player takes the score does not use the total scores but the scores from that individual turn.
    currentUserScore = 0
    currentComputerScore = 0

    #This if else if statement updates the scores depending on if the player/computer matches the answer.
    if answer == userChoice:
        currentUserScore = int(currentUserScore) + 1
        totalUserScore = int(totalUserScore) + 1
    elif answer == computerChoice:
        currentComputerScore = int(currentComputerScore) + 1
        totalComputerScore = int(totalComputerScore) + 1

    # This statement prints the statement for each winner depending on who has the score 1 in each round and will then print the total score and ask if they want to play again.
    if currentUserScore > currentComputerScore:
        print('You have won this round and the computer has lost! Your total score so far is: ' + str(totalUserScore) + ' point(s) and the computers total score is: ' + str(totalComputerScore) + '\nWould you like to play again?')
        playAgain = input()
        if playAgain.upper() == 'YES':
            beginGame()
    elif currentComputerScore > currentUserScore:
        print('You have lost this round and the computer has won! Your total score so far is: ' + str(totalUserScore) + ' point(s) and the computers total score is: ' + str(totalComputerScore) + '\nType yes to play again!')
        playAgain = input()
        if playAgain.upper() == 'YES':
            beginGame()

beginGame()