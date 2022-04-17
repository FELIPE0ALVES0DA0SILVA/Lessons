import random

x = random.randint(1, 50)
myList = ['rock', 'paper', 'scissor']
z = random.choice(myList)
print(z)
desordem = [1, 2, 3, 4, 5, 6, 'A', 'B', 'C', 'D']
random.shuffle(desordem)
print(desordem)
