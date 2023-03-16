from flask import Flask, request, render_template, redirect, url_for, json, escape
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
=======
>>>>>>> 16863da91af4ea366abe34e58e7b1ca57ccb7ddc
import os
import subprocess


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

<<<<<<< HEAD
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"

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
        min=4, max=20)], render_kw ={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw ={"placeholder": "Password"})    

    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw ={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw ={"placeholder": "Password"})    

    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()

        if existing_user_username:
            raise ValidationError("Username already Exists.")

@app.route("/settings", methods=["GET", "POST"])
@login_required
=======
@app.route("/settings", methods=["GET", "POST"])
>>>>>>> 16863da91af4ea366abe34e58e7b1ca57ccb7ddc
def settings():
    if request.method == "POST":
        helligkeit = request.form["Helligkeit"]
        geschwindigkeit = request.form["Geschwindigkeit"]
        text = request.form["Text"]
        wlan = request.form["WLAN-Name"]
        wlanpw = request.form["WLAN-Passwort"]

        text = text.replace('\r', ', ').replace('\n', '')
        stringsss = ["12","321","321"]
        print(text)
<<<<<<< HEAD
=======

        jsonstring = "{\"Helligkeit\":" + "\"" + helligkeit + "\", " + "\"Geschwindigkeit\":" + "\"" + geschwindigkeit + "\", " + "\"Text\":" + "\"" + text + "\", " + "\"WLAN\":" + "\"" + wlan + "\", ""\"WLAN-Passwort\":" + "\"" + wlanpw + "\"}"
        data = eval(jsonstring)
        print(jsonstring)
>>>>>>> 16863da91af4ea366abe34e58e7b1ca57ccb7ddc

        jsonstring = "{\"Helligkeit\":" + "\"" + helligkeit + "\", " + "\"Geschwindigkeit\":" + "\"" + geschwindigkeit + "\", " + "\"Text\":" + "\"" + text + "\", " + "\"WLAN\":" + "\"" + wlan + "\", ""\"WLAN-Passwort\":" + "\"" + wlanpw + "\"}"
        data = eval(jsonstring)
        print(jsonstring)
        #print(data['Helligkeit'])
        #print(jsonstring)

<<<<<<< HEAD
        with open("./inputs.json", "w") as fo:
=======
        with open("./Flasksite/inputs.json", "w") as fo:
>>>>>>> 16863da91af4ea366abe34e58e7b1ca57ccb7ddc
            fo.write(jsonstring)

        return f"""
        <h3>Folgende Werte wurden eingegeben:</h3>
        <ul>
            <li>Helligkeit:{escape(helligkeit)}</li>
            <li>Geschwindigkeit: {escape(geschwindigkeit)}</li>
            <li>WLAN-Name:{escape(wlan)}</li>
            <li>WLAN-Passwort:{escape(wlanpw)}</li>
            <li>Text:</li>
        </ul>
<<<<<<< HEAD
=======
        
>>>>>>> 16863da91af4ea366abe34e58e7b1ca57ccb7ddc
        <a href="{"/"}"> Zurück zum Hauptmenü </a>
        """
    return render_template("settings.html")

<<<<<<< HEAD
@app.route("/load", methods=["GET", "POST"])
@login_required
def load():
    with open("./inputs.json") as json_file:
        data = json.load(json_file)

    os.system("sudo sh runScript.sh")
=======

@app.route("/load", methods=["GET", "POST"])
def load():
    with open("./Flasksite/inputs.json") as json_file:
        data = json.load(json_file)
>>>>>>> 16863da91af4ea366abe34e58e7b1ca57ccb7ddc

    return f"""
    <H3>Folgende Daten Geladen:</h3> 
    <ul>
        <li>Helligkeit:{escape(data['Helligkeit'])}</li>
        <li>Geschwindigkeit:{escape(data['Geschwindigkeit'])}</li>
        <li>Wlanname:{escape(data['WLAN'])}</li>
        <li>Wlanpasswort:{escape(data['WLAN-Passwort'])}</li>
        <li>Text:{escape(data['Text'])}</li>
    </ul>
<<<<<<< HEAD
    <a href="{"/"}">Zurück zum Hauptmenü</a>
    """

@app.route("/home")
=======

    <a href="{"/"}">Zurück zum Hauptmenü</a>
    """

@app.route("/")
>>>>>>> 16863da91af4ea366abe34e58e7b1ca57ccb7ddc
def home():
    return render_template("index.html")

@app.route("/")
def index():
    return redirect(url_for('home'))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))
    return render_template("login.html", form = form)

@app.route("/register", methods=["GET", "POST"])
@login_required
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("register.html", form = form)


if __name__ == "__main__":

    app.run()

