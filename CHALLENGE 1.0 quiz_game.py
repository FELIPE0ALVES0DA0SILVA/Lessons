# ----------------------
def new_game(questions, options):
    unswers = []
    count = 0
    score = 0
    for key in questions:
        confirmation = False
        print('-----------------')
        print(key)
        for value in options[count]:
            print(value)
        count += 1
        while confirmation != True:
            unswer = input('Unswer => ').upper()
            unswer = unswer[0]
            alternatives = ['A', 'B', 'C', 'D']
            if unswer in alternatives:
                unswers.append(unswer)
                confirmation = True
            else:
                print('Typ the correct unswer!')
        score += check_answer(unswer, question.get(key))
    print(unswers)
    print('You have scored ' + str(score) + ' from 3 guesses, congrats!')


# ----------------------


def check_answer(unswer, guess):
    if unswer == guess:
        print("CORRECT")
        return 1
    else:
        print('WRONG')
        return 0
# ----------------------


def display_score():
    pass
# ----------------------


def play_again():
    pass


question = {
    'Who created Python?': 'A',
    'What year was Python created?': 'B',
    'Python is tributed to which comedy group?': 'C',
    'Is the earth round?': 'A',
}

options = [
    ['A. Guido van rossum', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark Zuckenberg'],
    ['A. 1898', 'B. 1991', 'C. 2000', 'D. 2006'],
    ['A. Lonely island', 'B. Smosh', 'C. Monty Python', 'D. SNL'],
    ['A. True', 'B. False', 'C. False', 'D. False'],
]

new_game(question, options)
