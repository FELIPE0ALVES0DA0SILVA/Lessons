import random

choices = ['rock', 'paper', 'scissor']

computer = random.choice(choices)


user = None
while user != 'N':
    player = None
    while player not in choices:
        player = input('Rock, Paper, or Scissor! => ').lower()

    print('Computer: ', computer)
    print('Player: ', player)

    if player == computer:
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('The computer loose!')
        if computer == 'scissor':
            print('The computer won!')
    elif player == 'scissor':
        if computer == 'paper':
            print('The computer loose!')
        if computer == 'rock':
            print('The computer won!')
    elif player == 'paper':
        if computer == 'rock':
            print('The computer loose!')
        if computer == 'scissor':
            print('The computer won!')
    while user != 'S' or user == 'N':
        user = input('Do you want to play again? [S/N] ').upper()
        user = user[0]
        print(user)
