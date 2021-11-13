from flask import Flask, render_template, request
from helpers import assign_name, user

app: Flask = Flask(__name__)
users: list[user] = []
user_number: int = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/todo', methods=["GET", "POST"])
def todo():
    global users
    global user_number
    
    return render_template("todo.html")





@app.route('/add_assign', methods=["GET", "POST"])
def add_assign():
    if request.method == "POST":
        global users
        global user_number

        assignment: str = request.form['assignment']

        # assign_name: str = request.form['assignment']

        if assign_name == '':
            return render_template("add_assign.html")

        name: str = assign_name(assignment)
        new_user: user = user(user_number, assignment, name)
        users.append(new_user)

        user_number += 1

        return render_template("todo.html", name=name)
    return render_template("add_assign.html")

@app.route('/all-results')
def all_results():
    return render_template('all-results.html', users=users)

@app.route('/user<usernumber>')
def display_user(usernumber: str):
    return render_template('user.html', user=users[int(usernumber)])


if __name__ == '__main__':
    app.run(debug=True)