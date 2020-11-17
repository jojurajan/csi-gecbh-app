from flask import render_template, redirect, flash, url_for, request
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {
        "username": "Joju"
    }
    print(request.args)
    if request.args:
        user = {
            "username": request.args["username"]
        }
    data = [
        {
            "subject": "Physics",
            "marks": 30
        },
        {
            "subject": "Maths",
            "marks": 35
        },
        {
            "subject": "Chemistry",
            "marks": 32
        }
    ]
    return render_template("index.html", title="Home", user=user, data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("index", username=form.data["username"]))
    return render_template("login.html", title="Sign In", form=form)
