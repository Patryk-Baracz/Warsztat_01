from random import randint

secret_numbers = []
player_numbers = []
score = 0
for i in range(0, 6):
    while True:
        secret_number = randint(1, 49)
        if secret_number in secret_numbers:
            continue
        else:
            secret_numbers.append(secret_number)
            break

print('Please pick 6 numbers in range 1 to 49.')

for i in range(0, 6):
    while True:
        answer = input(f'Number #{i+1}:')
        if not answer.isdigit():
            print("Your number has to be an integer! Try again.")
            continue
        elif int(answer) < 1 or int(answer) > 49:
            print("Your number has to be in range 1 to 49! Try again.")
            continue
        elif int(answer) in player_numbers:
            print(f"You have already picked {answer}. Pick another number.")
        else:
            player_numbers.append(int(answer))
            break

print(f'Your numbers : {player_numbers}')
print(f'Lucky numbers : {secret_numbers}')
for i in player_numbers:
    if i in secret_numbers:
        score += 1
print(f'You have hit {score}!')
