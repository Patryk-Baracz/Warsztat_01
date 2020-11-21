from random import randint

secret_number = randint(1, 100)
player_number = None

while player_number != secret_number:
    player_number = input('Guess the number (1-100):')
    try:
        player_number = float(player_number)
    except ValueError:
        print('It\'s not a number!')
        continue
    if player_number % 1 != 0:
        print('It\'s not an integer!')
        continue
    else:
        if player_number <= 0 or player_number > 100:
            print('It\'s out of range!')
        elif player_number < secret_number:
            print("To small!")
        elif player_number > secret_number:
            print("To big!")


print("You win!")
