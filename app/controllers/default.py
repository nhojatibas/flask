from flask import render_template
from app import app

from app.models.forms import LoginForm


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    print("Form"+str(form))
    if form.validate_on_submit():
        print(form.username.data)   
        print(form.password.data)
    return render_template('login.html',
                            form=form)
