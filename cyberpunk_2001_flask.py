from flask import Flask, request, render_template
import random


app = Flask(__name__)


def roll_dice(dice_type):
    d_list = [3, 4, 6, 8, 10, 12, 20, 100]
    if int(dice_type) not in d_list:
        raise ValueError(f"There are no {dice_type}D dice's")
    return random.randint(1, int(dice_type))


def player_turn():
    d1 = int(request.form['dice_1'])
    d2 = int(request.form['dice_2'])
    return roll_dice(d1) + roll_dice(d2)


def computer_turn():
    c1 = random.choice([3, 4, 6, 8, 10, 12, 20, 100])
    c2 = random.choice([3, 4, 6, 8, 10, 12, 20, 100])
    return roll_dice(c1) + roll_dice(c2)


@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        return render_template('Cyberpunk_2001.html', computer_points='0', player_points='0')
    else:
        player_points = int(request.form['player_p'])
        computer_points = int(request.form['computer_p'])
        if player_points == 0:
            player_points += player_turn()
            computer_points += computer_turn()
            return render_template('Cyberpunk_2001.html', computer_points=str(computer_points),
                                       player_points=str(player_points))
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
        if player_points > 2001:
            return render_template('Cyberpunk_2001.html', computer_points=str(computer_points), player_points='You won!')
        elif computer_points > 2001:
            return render_template('Cyberpunk_2001.html', computer_points='Computer won!',
                                   player_points=str(player_points))
        else:
            return render_template('Cyberpunk_2001.html', computer_points=str(computer_points),
                                   player_points=str(player_points))


app.run(debug=True)
