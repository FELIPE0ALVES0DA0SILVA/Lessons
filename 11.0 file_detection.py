import os

path = 'C:\\PYTHON\\lessons'

if os.path.exists(path):
    print('Exist')
    if os.path.isfile(path):
        print('Is a File')
    elif os.path.isdir(path):
        print('Is a directory')
    else:
        print('Its not a file')
else:
    print('DO not exist.')
