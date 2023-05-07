from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
# import sqlite3
import requests
from datetime import date, datetime
from forex_python.converter import CurrencyRates
import re
from speech import Speech
import time

currency = CurrencyRates()
s = Speech()
s.Text2Speech("init")

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# dbs = sqlite3.connect("users.db")

# cursor = dbs.cursor()


#to be codded 
#login manager
# def load_user(user_id):
#     return User.query.get(int(user_id))


#Database Table Creation Section
# app.app_context().push()

#to create tables
#inside terminal
# from server import app, db
# app.app_context().push()
# db.create_all()

#Sign up table which contains data of user
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    phoneno = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))


# cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username varchar(250) NOT NULL UNIQUE, fname varchar(250), lname varchar(250), phoneno varchar(250), email varchar(250), password varchar(250))")
   
    # usernamess = db.relationship('userBalance', backref='user')

class remBal(db.Model):
    # __tablename__ = "users_balances"
    # username = db.Column(db.String(100), primary_key=True, db.ForeignKey('user.username'))
    username = db.Column(db.String(100), primary_key=True)
    balance = db.Column(db.Integer)

# cursor.execute("CREATE TABLE balances (username varchar(250) PRIMARY KEY, balance INTEGER)")

class clientTranscation(db.Model):
    # __tablename__ = "client_transcation"
    transcation_id = db.Column(db.String(100), primary_key=True)
    f_username = db.Column(db.String(100))
    t_username = db.Column(db.String(100))
    amount = db.Column(db.String(100))
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))

class lnAct(db.Model):
    # __tablename__ = "users_balances"
    # username = db.Column(db.String(100), primary_key=True, db.ForeignKey('user.username'))
    username = db.Column(db.String(100), primary_key=True)
    debt = db.Column(db.Integer)
    credits = db.Column(db.Integer)
    score = db.Column(db.Integer)

class lnTranscation(db.Model):
    # __tablename__ = "client_transcation"
    transcation_id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(100))
    amount = db.Column(db.String(100))
    rem_debt = db.Column(db.Integer)
    intrest = db.Column(db.Integer)
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))

class Erng(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    loan_intrest = db.Column(db.Integer)
    transcationm_intrest = db.Column(db.Integer)
    topup_fee = db.Column(db.Integer)
    total = db.Column(db.Integer)
    
class Admin(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))

class BnkAcc(db.Model):
    # __tablename__ = "client_transcation"
    ac_no = db.Column(db.Integer, primary_key=True)
    ifsc = db.Column(db.String(100))
    balance = db.Column(db.Integer)

#other class section




@app.route("/login_or_sign_up", methods=["GET", "POST"])
def login_or_sign_up():

    #login
    if request.method == "POST":
        if request.form["submit"] == "log_in":


            l_username = request.form["l_username"]
            l_password = request.form["l_password"]
            print(l_username, l_password) 

            user = User.query.filter_by(username=l_username).first()
            if not user:
                flash("this username does not exist, Please Register")
                return redirect(url_for('login_or_sign_up'))
            elif not check_password_hash(user.password, l_password):
                flash("Password incorrect, PLease Try Again")
                return redirect(url_for('login_or_sign_up'))
            else:
                return redirect(url_for('home'))
        
        #sign up
        if request.form["submit"] == "Sign_up":

            if User.query.filter_by(username=request.form.get('s_username')).first():
            #User already exists
                flash("You've already signed up with that username, log in instead!")
                return redirect(url_for('login_or_sign_up'))


            s_username = request.form["s_username"]
            s_fname = request.form["s_fname"]
            s_lname = request.form["s_lname"]
            s_phoneno = request.form["s_phoneno"]
            s_email = request.form["s_email"]
            s_password = request.form["s_password"]
            print(s_username, s_fname, s_lname, s_phoneno, s_email, s_password)



            hash_and_salted_password = generate_password_hash(
                s_password,
                method='pbkdf2:sha256',
                salt_length=8
            )

            new_user = User(
                username = s_username,
                fname = s_fname,
                lname = s_lname,
                phoneno = s_phoneno,
                email = s_email,
                password = hash_and_salted_password
            )
            db.session.add(new_user)
            db.session.commit()

            # cursor.execute(f"INSERT INTO users VALUES({s_username}, {s_fname}, {s_lname}, {s_phoneno}, {s_email}, {hash_and_salted_password})")

            
            # cursor.execute(f"INSERT INTO balances VALUES({s_username}, 100)")
            return redirect(url_for("home"))

            #database of new user
            # modelName = s_username + "db"
            # class modelName(db.Model):
            #     transcation_id = db.Column(db.Integer, primary_key=True)
            #     transaction_amt = db.Column(db.Integer)
            #     remaning_amt = db.Column(db.Integer)
            # # db.create_all()
            # modelName.__table__.create(db.session.bind, checkfirst=True)

            print("new user data inserted into database")

    return render_template("login.html")

@app.route("/")
def main():
    return redirect(url_for('login_or_sign_up'))


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/location")
def location():
    return render_template("location.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        chat = request.form["chat"]
        print(chat)
        # time.sleep()
        s.Text2Speech(f"received message {chat} from parental control")
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)

