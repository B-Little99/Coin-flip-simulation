import math, random

userChoice = ''
computerChoice = ''
answer = ''
currentUserScore = 0
currentComputerScore = 0
totalUserScore = 0 
totalComputerScore = 0

print('Welcome to the coin flip game. You will play against a computer to see who has the best luck!')

def beginGame():
    global userChoice
    global answer
    global computerChoice
    print('Would you like to be Heads or Tails?')
    userDecision = str(input())

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

    randomNumber = random.randint(0, 1)

    if randomNumber == 0:#> 50:
        print('It\'s heads!')
        answer = 'Heads'
        resultScore()
    elif randomNumber == 1:#randomNumber >= 1 and randomNumber <= 50:
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

    currentUserScore = 0
    currentComputerScore = 0

    if answer == userChoice:
        currentUserScore = int(currentUserScore) + 1
        totalUserScore = int(totalUserScore) + 1
    elif answer == computerChoice:
        currentComputerScore = int(currentComputerScore) + 1
        totalComputerScore = int(totalComputerScore) + 1

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