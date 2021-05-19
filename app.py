from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import os
from forms import RegistrationForm, LoginForm, UploadRecipeForm, EditProfileForm
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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
    # validate on submit
    if form.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {"username": request.form["username"].lower()})
        # cehck for the excisting user
        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["existing_user"] = request.form["username"]
                flash('Hi {}!'.format(session['existing_user']))
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


@app.route("/sign_out")
def sign_out():
    session.clear()
    flash('You have been successfully logged out!')
    return redirect(url_for('index'))


@app.route("/upload_recipe", methods=["GET", "POST"])
def upload_recipe():
    if (session.get('existing_user') is None):
        flash('Please sign in to upload a recipe!')
        return redirect(url_for('login'))

    form = UploadRecipeForm(request.form)

    if form.validate_on_submit():
        recipe = {
            'image': request.form['image'],
            'recipe_title': request.form['recipe_title'],
            'recipe_story': request.form['recipe_story'],
            'ingredients': request.form['ingredients'],
            'steps': request.form['steps'],
            'categories': request.form['categories'],
            'keto_recipe': request.form['keto_recipe']}
        mongo.db.recipes.insert_one(recipe)

        flash('Your recipe was seccessfuly added to your collection!')
        return redirect(url_for('index'))
    return render_template("upload_recipe.html", title='Upload', form=form)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    form = EditProfileForm(request.form)

    return render_template("profile.html", title='Profile', form=form)


@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    form = EditProfileForm(request.form)

    return render_template("edit_profile.html", title='Profile', form=form)


@app.route("/all_recipes", methods=["GET"])
def all_recipes():
    # Check if we have `type` argument in the request
    recipe_type = request.args.get('type')
    if recipe_type is None:
        all_recipes = mongo.db.recipes.find()
        return render_template("all_recipes.html", title='All-Recipes', recipes=all_recipes)
    if recipe_type == 'keto':
        recipes = mongo.db.recipes.find({'keto_recipe': True})
        return render_template("all_recipes.html", title='Keto', recipes=recipes)
    specific_recipes = mongo.db.recipes.find({"categories": recipe_type})
    return render_template("all_recipes.html", title=recipe_type, recipes=specific_recipes)


@app.route("/search")
def search():
    search = request.args('query')
    if search is True:
        search_result = mongo.db.recipes.find({
            'recipes.title': search,
            'recipes.recipe_story': search,
            'recipes.recipe_ingredients': search
        })
    return render_template("all_recipes.html", search=search_result)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
