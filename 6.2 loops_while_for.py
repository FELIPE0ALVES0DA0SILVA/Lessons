phone_number = '1234-5678-91011'

for i in phone_number:
    if i == '-':
        continue
    print(i, end='')
