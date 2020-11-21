from flask import Flask, render_template, request

app = Flask(__name__)

def guess(max_l, min_l):
    return int((int(max_l) - int(min_l)) / 2 + int(min_l))



@app.route('/', methods = ["GET", "POST"])
def zgadywanka():
    if request.method == 'GET':
        return render_template('zgadywanka.html')
    else:

        if request.form['value'] == "You won":
            return render_template('zgadywanka.html', comp_guess="Hurray! I won!")
        elif request.form['value'] == "To big":
            min_l = request.form['min_value']
            max_l = guess(request.form['max_value'], request.form['min_value'])
            guess_v = guess(max_l, min_l)
            return render_template('zgadywanka.html', comp_guess=str(guess_v), min_value=str(min_l), max_value=str(max_l))
        elif request.form['value'] == "To small":
            min_l = guess(request.form['max_value'], request.form['min_value'])
            max_l = request.form['max_value']
            guess_v = guess(max_l, min_l)
            return render_template('zgadywanka.html', comp_guess=str(guess_v), min_value=str(min_l), max_value=str(max_l))
        else:
            min_l = 0
            max_l = 1000
            guess_v = guess(max_l, min_l)
            return render_template('zgadywanka.html', comp_guess=str(guess_v), min_value=str(min_l), max_value=str(max_l))


app.run(debug=True)
