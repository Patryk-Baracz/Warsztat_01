print("""Imagine a number from 0 to 1000, and i will guess it in max 10 tries.
Press ENTER when ready""")
input()
min_l = 0
max_l = 1000
while True:
    guess = int((max_l - min_l) / 2 + min_l)
    print(f'My guess: {guess}')
    print('Am I right?')
    respond = input('Type: "You win", "to big" or "to small"').lower()
    if respond == 'you win':
        break
    elif respond == 'to big':
            max_l = guess

    elif respond == 'to small':
        min_l = guess
    else:
        print("Don't cheat!")

print('Hurray! I won!')
