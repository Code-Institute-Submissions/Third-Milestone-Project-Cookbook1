from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import os
from forms import RegistrationForm, LoginForm, UploadRecipeForm, EditRecipeForm, DeleteRecipeForm
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
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
            flash("This username already exists. Please choose another name!")
            return redirect(url_for("register"))

        # registration and hasing password
        hassed_password = generate_password_hash(request.form["password"])
        registration = {
            "username": request.form["username"].lower(),
            "password":  hassed_password}
        mongo.db.users.insert_one(registration)

        # put the user into session cookie and return back to index page
        session["existing_user"] = request.form["username"].lower()
        flash(
            'Registration was seccessful! Welcome to the community {}!'.format
            (request.form.get("username")))
        return redirect(url_for('index'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    # validate on submit
    if form.validate_on_submit():
        existing_user = mongo.db.users.find_one(
            {"username": request.form["username"].lower()})
        # cehck for the excisting user in database
        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["existing_user"] = request.form["username"]
                flash('Hi {}!'.format(session.get("existing_user")))
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
    # Clear session to sign user out
    session.clear()
    flash('You have been successfully logged out!')
    return redirect(url_for('index'))


@app.route("/upload_recipe", methods=["GET", "POST"])
def upload_recipe():
    # If no user in session flash message to sign in
    if (session.get('existing_user') is None):
        flash('Please sign in to upload a recipe!')
        return redirect(url_for('login'))

    form = UploadRecipeForm(request.form)
    '''Validate on submit if user in session and
    upload data to database from Upload recipe form'''
    if form.validate_on_submit():
        recipe = {
            'image': request.form['image'],
            'recipe_title': request.form['recipe_title'],
            'author': session.get("existing_user"),
            'recipe_story': request.form['recipe_story'],
            'ingredients': request.form['ingredients'],
            'steps': request.form['steps'],
            'categories': request.form['categories'],
            'keto_recipes': request.form['keto_recipes']}
        # Insert data to database
        mongo.db.recipes.insert_one(recipe)
        # Flas message to cinfirm recipe upload
        flash('Your recipe was seccessfuly added to your collection!')
        return redirect(url_for('index'))
    return render_template("upload_recipe.html", title='Upload', form=form)


@app.route("/edit_recipe/<recipe_id>",  methods=["GET", "POST"])
def edit_recipe(recipe_id):
    form = EditRecipeForm(request.form)
    recipe_data = mongo.db.recipes.find_one_or_404(
        {'_id': ObjectId(recipe_id)})
    # If user logged in allow them to edit their recipe
    if request.method == "GET":
        form = EditRecipeForm(data=recipe_data)
        return render_template('edit_recipe.html', recipe=recipe_data,
                               form=form)
        # On submit enter editted data to database
    if request.method == "POST" and form.validate_on_submit():
        recipe = {
            "$set": {
                'image': request.form['image'],
                'recipe_title': request.form['recipe_title'],
                'author': session.get("existing_user"),
                'recipe_story': request.form['recipe_story'],
                'ingredients': request.form['ingredients'],
                'steps': request.form['steps'],
                'categories': request.form['categories'],
                'keto_recipes': request.form['keto_recipes']}}
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, (recipe))
        flash('Your recipe has been updated!')
    return render_template("recipe.html", recipe=recipe_data, form=form)


@app.route("/all_recipes", methods=["GET"])
def all_recipes():
    # Check if we have `type` argument in the request
    recipe_type = request.args.get('type')
    # If there is no specific type was requested return back to all recipes
    if recipe_type is None:
        all_recipes = mongo.db.recipes.find()
        return render_template("all_recipes.html", title='All-Recipes',
                               recipes=all_recipes)
    '''If recipe type is keto and in the database strings = yes,
         return back all keto recipes'''
    if recipe_type == 'keto':
        recipes = mongo.db.recipes.find({'keto_recipe': 'yes'})
        return render_template("all_recipes.html", title='Keto',
                               recipes=recipes)
    '''If session user is the same as the author of the recipe,
        then return back all those recipes to my recipes'''
    if recipe_type == 'my_recipes':
        active_user = session['existing_user']
        recipes = mongo.db.recipes.find({'author': active_user})
        return render_template("all_recipes.html", title='My Profile',
                               recipes=recipes)
    '''If any recipe type was requested then return back
        to the requested type page with the same type recipes'''
    specific_recipes = mongo.db.recipes.find({"categories": recipe_type})
    return render_template("all_recipes.html", title=recipe_type,
                           recipes=specific_recipes)


@app.route("/search")
def search():
    # If request query
    search = request.args.get('query')
    # Search recipe title, story,ingrediesnts and cathegory for the request
    search_result = mongo.db.recipes.find({
        '$or': [
            {'recipe_title': {'$regex': search}},
            {'recipe_story': {'$regex': search}},
            {'ingredients': {'$regex': search}},
            {'categories': {'$regex': search}}
        ]})
    # If result is none direct ti index page and display flash message
    if search_result.count() == 0:
        flash('No {} found in recipes, please make a new search!'
              .format(search))
        return redirect(url_for('index'))
    return render_template("all_recipes.html", query=search,
                           recipes=search_result)


@app.route("/delete_recipe/<recipe_id>",  methods=["GET", "POST"])
def delete_recipe(recipe_id):
    form = DeleteRecipeForm(request.form)
    recipe_data = mongo.db.recipes.find_one_or_404(
        {'_id': ObjectId(recipe_id)})
    # Allow author to delete their recipe
    if request.method == "GET":
        form = DeleteRecipeForm(data=recipe_data)
        return render_template('delete_recipe.html', recipe=recipe_data,
                               form=form)
    if request.method == "POST" and form.validate_on_submit():
        mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
        flash('Your recipe has been deleted!')
        return redirect(url_for('all_recipes', type='my_recipes'))
    return render_template("delete_recipe.html", title=delete_recipe,
                           recipe=recipe_data, form=form)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    # Pull specific recipe from the database
    recipe_data = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe_data)


@app.errorhandler(404)
def handle_404():
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
