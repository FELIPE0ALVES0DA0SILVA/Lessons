
try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number divide by zero: '))

    result = numerator / denominator

except ZeroDivisionError:
    print("You can't divide by zero, bro!")
except ValueError:
    print('Enter only numbers please!')
else:
    print(result)
finally:
    print('Will always execute.')
