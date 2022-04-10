age = int(input('How old are you? '))

if age >= 18 and age < 100:
    print('You are an Adult!')
elif age <= 0:
    print("You haven't born yet!")
elif age == 100:
    print("You are a century old man!")
else:
    print('you are a Muslim!')
