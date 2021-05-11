import os
from forms import RegistrationForm, LoginForm
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm(request.form)
    # validate on submit
    if form.validate_on_submit():
        # check for excisting user
        existing_user = mongo.db.users.find_one(
            {"username": request.form["username"].lower()})

        if existing_user:
            flash("This username already excist. Please choose another name!")
            return redirect(url_for("register"))

        # registration
        hassed_password = generate_password_hash(request.form["password"])
        registration = {
            "username": request.form["username"].lower(),
            "password":  hassed_password}
        mongo.db.users.insert_one(registration)

        # put the user into session cookie
        session["username"] = request.form["username"].lower()
        flash(
            'Registration was seccessful! Welcome to the community {}!'.format(request.form.get("username")))
        return redirect(url_for('index'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user:
            if check_password_hash(
                    user["password"], request.form.get("password")):
                session["user"] = request.form.get("username".lower())
                flash('Hi {}!'.format(request.form.get("username")))
                return redirect(url_for('index'))
            else:
                # invalid password
                flash("Incorrect Username and/or Password, please try again!")
                return redirect(url_for('login'))
        else:
            # invalid username
            flash("Incorrect Username and/or Password, please try again!")
            return redirect(url_for('login'))

    return render_template("login.html", title='Login', form=form)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
