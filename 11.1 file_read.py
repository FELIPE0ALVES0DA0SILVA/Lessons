import shutil

try:
    text = 'Yoooo\nMy name is Felipe'
    text2 = '\nI am amazing'
    with open('C:\\PYTHON\\new.txt', 'w') as file:
        file.write(text)
    with open('C:\\PYTHON\\new.txt', 'a') as file:
        file.write(text2)

    shutil.copyfile('C:\\PYTHON\\new.txt', 'new.txt')
except FileNotFoundError:
    print('That file doesnt exists')
