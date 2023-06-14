from flask import Flask, request, render_template, redirect, url_for, json, escape
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import signal
import os
import subprocess

pid_drehteller = 0
drehteller_running = False

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()

        if existing_user_username:
            raise ValidationError("Username already exists.")

@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    print(request.method)
    if request.method == "POST":
        print("AHHAAAH")
        helligkeit = request.form["Helligkeit"]
        geschwindigkeit = request.form["Geschwindigkeit"]
        text = request.form["Text"]
        print("AHHAAAH")

        text = text.replace('\r', ', ').replace('\n', '')

        jsonstring = "{\"Helligkeit\":" + "\"" + helligkeit + "\", " + "\"Geschwindigkeit\":" + "\"" + geschwindigkeit + "\", " + "\"Text\":" + "\"" + text + "\"}"
        data = eval(jsonstring)
        print(jsonstring)

        with open("./inputs.json", "w") as fo:
            fo.write(jsonstring)

        return render_template("settings.html", helligkeit=helligkeit, geschwindigkeit=geschwindigkeit,
                               text=text)

    return render_template("settings.html")

@app.route("/load", methods=["GET", "POST"])
@login_required
def load():
    drehteller_running = True
    with open("./inputs.json") as json_file:
        data = json.load(json_file)

    os.system("sudo sh runScript.sh")
    try:
        pid_drehteller = subprocess.run(
            ['sudo', 'sh', './runScript.sh']).pid
    except FileNotFoundError:
        print("Datei wurde nicht gefunden.")
        return "Datei nicht gefunden."

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/")
def index():
    return redirect(url_for('home'))

@app.route("/reboot",methods=['GET', 'POST'])
@login_required
def restart():
    os.system('sudo reboot')
    return redirect(url_for('home'))

@app.route("/login.html", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    print(form.validate_on_submit())
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))

    return render_template("login.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/register.html", methods=["GET", "POST"])
@login_required
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(
            username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route("/stop", methods=["GET", "POST"])
@login_required
def stop():
    global drehteller_running
    if drehteller_running == 1:
        drehteller_running = 0
        drehteller_process = subprocess.Popen(['python','./drehteller2.py'])
        return f"""Application started successfully!
        <a href="{"/"}"> Zurück zum Hauptmenü </a>
        """
    else:
        return f"""Drehteller Läuft nicht!
        <a href="{"/"}"> Zurück zum Hauptmenü </a>
        """
    

if __name__ == "__main__":
    app.run()
