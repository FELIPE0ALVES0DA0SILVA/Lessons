rows = int(input('How many rows? '))
columns = int(input('How many columns? '))
symbol = input('Enter a symbol: ')

for i in range(rows):
    for j in range(columns):
        if j == columns-1:
            print(symbol)
            break
        print(symbol, end='--')
    print()
