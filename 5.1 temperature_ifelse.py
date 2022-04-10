temp = int(input('What is the temperature today? '))

if temp >= 0 and temp <= 30:
    print('the temperature is good today')
    print('go outside please!')
elif temp < 0 and temp >= -15:
    print("It's very cold, please warm yourself!")
else:
    print('Please get out from the earth!')
