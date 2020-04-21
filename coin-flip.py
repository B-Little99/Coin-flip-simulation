import math, random

def beginGame():
    print('Welcome to the coin flip game. You will play against a computer to see who has the best luck! Would you like to be Heads or Tails?')
    userDecision = str(input())
    userPlayer = ''
    computerPlayer = ''
    user = ''
    computer = ''

    if userDecision.upper() == 'HEADS':
        userPlayer = 'Heads'
        computerPlayer = 'Tails'
    elif userDecision.upper() == 'TAILS':
        userPlayer = 'Tails'
        computerPlayer = 'Heads'
    else:
        print('Please state whether you want to be heads or tails')
        beginGame()

    print('You have selected ' + userPlayer + ', so the computer will be ' + computerPlayer + '.')

def playGame(): 
    randomNumber = random.randint(0, 1)
    print(randomNumber)
    if randomNumber == 0:
        print('It\'s heads!')
    elif randomNumber == 1:
        print('It\'s tails!')







beginGame()
playGame()


