import os

source = 'new_2.txt'
destination = 'C:\\PYTHON\\new_2.txt'

try:
    if os.path.exists(destination):
        print('This directory and file exist')
    else:
        os.replace(source, destination)
        print(source + 'was moved')
except FileNotFoundError:
    print('This file doesnt exists')
