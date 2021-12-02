from flask import Flask, render_template, request
from helpers import find_animal, user

# run the website by typing 'python -m app'

app: Flask = Flask(__name__)
users: list[user] = []
user_number: int = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        global users
        global user_number

        fname: str = request.form ['fname']
        lname: str = request.form['lname']
        personality: str = request.form['personality']
        realm: str = request.form['realm']
        color: str = request.form['color']
        music: str = request.form['music']
        power: str = request.form['power']
        princess: str = request.form['princess']
        holiday: str = request.form['holiday']

        if fname == '' or lname == '' or personality == '' or realm == '' or color == '' or music == '' or power == '' or princess == '' or holiday == '':
            return render_template("quiz.html")

        animal: str = find_animal(music)
        new_user: user = user(user_number, fname, lname, animal)
        users.append(new_user)

        user_number += 1

        return render_template("result.html", animal=animal)
    return render_template("quiz.html")

@app.route('/all-results')
def all_results():
    return render_template('all-results.html', users=users)

@app.route('/user<usernumber>')
def display_user(usernumber: str):
    return render_template('user.html', user=users[int(usernumber)])

if __name__ == '__main__':
    app.run(debug=True)