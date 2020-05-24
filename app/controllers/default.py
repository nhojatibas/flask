from flask import render_template
from app import app

from app.models.forms import LoginForm


@app.route("/index")
@app.route("/")
def index():
    print("Index")
    return render_template('index.html')

@app.route("/main")
def main():
    print("Nerso")
    return render_template('main.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    app.logger.warning('Form..: '+str(form))
    if form.validate_on_submit():
        app.logger.warning('Username..: '+str(form.username.data))
        app.logger.warning('Senha.....: '+str(form.password.data))
    return render_template('login.html',
                            form=form)

@app.route('/print')
def printMsg():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    return "Check your console"
