import random


def roll_dice(dice_type):
    d_list = [3, 4, 6, 8, 10, 12, 20, 100]
    if int(dice_type) not in d_list:
        raise ValueError(f"There are no {dice_type}D dice's")
    return random.randint(1, int(dice_type))


def player_turn():
    d_list = [3, 4, 6, 8, 10, 12, 20, 100]
    while True:
        d1 = input('Choose your first dice type (3, 4, 6, 8, 10, 12, 20, 100):')
        if not d1.isdigit():
            print('You need to type a number!')
        elif int(d1) not in d_list:
            print('Choose a number from list above!')
        else:
            break
    while True:
        d2 = input('Choose your second dice type (3, 4, 6, 8, 10, 12, 20, 100):')
        if not d2.isdigit():
            print('You need to type a number!')
        elif int(d2) not in d_list:
            print('Choose a number from list above!')
        else:
            break
    value = roll_dice(d1) + roll_dice(d2)
    return value


def computer_turn():
    c1 = random.choice([3, 4, 6, 8, 10, 12, 20, 100])
    c2 = random.choice([3, 4, 6, 8, 10, 12, 20, 100])
    computer_value = roll_dice(c1) + roll_dice(c2)
    return computer_value


def game():
    player_points = 0
    computer_points = 0
    while True:
            if player_points >= 2001:
                break
            elif computer_points >= 2001:
                break
            else:
                print(f'computer points = {computer_points}')
                print(f'Your points = {player_points}')
                if player_points == 0:
                    player_points += player_turn()
                    computer_points += computer_turn()
                else:
                    player_score = player_turn()
                    computer_score = computer_turn()
                    if player_score == 7:
                        player_points = int(player_points / 7)
                    elif player_score == 11:
                        player_points = player_points * 11
                    else:
                        player_points += player_score
                    if computer_score == 7:
                        computer_points = int(computer_points / 7)
                    elif computer_score == 11:
                        computer_points = computer_points * 11
                    else:
                        computer_points += computer_score
    if player_points > computer_points:
        return 'You won!'
    else:
        return 'You lost!'


print(game())
