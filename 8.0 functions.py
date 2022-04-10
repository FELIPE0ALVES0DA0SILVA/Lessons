def hello(name):
    print('hello! ' + name)


def multiply(number1, number2):
    return number1 * number2


def arg(first, second, third):
    print('Hello ' + first+' '+second+' '+third)


def add(*args):
    sum = 0
    args = list(args)
    args[0] = 100
    for i in args:
        sum += i
    return sum


def kargs(**kwargs):
    print('Hello! ', end=' // ')
    for key, value in kwargs.items():
        print(value, end=' ')


kargs(alemane='Hoister', spanesh='Alvaroz', brasileiro='Felipão')
