from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectMultipleField
from wtforms import validators


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           [validators.InputRequired(),
                            validators.Length(min=5, max=15)])
    password = PasswordField('Password',
                             [validators.InputRequired(),
                              validators.Length(min=5, max=15)])
    confirm_password = PasswordField('Confirm Password',
                                     [validators.EqualTo('password',
                                                         message="Passwords should match")])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired(),
                                        validators.Length(min=5, max=15)])
    password = PasswordField('Password', [validators.InputRequired(),
                                          validators.Length(min=5, max=15)])
    remember_user = BooleanField('Stay Logged In')
    submit = SubmitField('Login')


class UploadRecipeForm(FlaskForm):
    image = FileField('Choose Image', [validators.DataRequired]),
    uplaod_img = SubmitField('Upload File'),
    recipe_title = StringField('Recipe Title', [
                               validators.InputRequired,
                               validators.Length(min=4, max=45)])
    recipe_story = TextAreaField('Add a short story...', [
                                 validators.DataRequired,
                                 validators.Length(min=5, max=200)])
    ingredients = StringField('Add ingredients by line', [
                              validators.InputRequired])
    steps = TextAreaField('Step by step method', [
                          validators.DataRequired,
                          validators.Length(min=5, max=260)])
    categories = SelectMultipleField('Recipe category (PLease select at least one)',
                                     choices=[('Breakfast'), ('Main meal'),
                                              ('Snacks')])
    keto_recipes = BooleanField('Is this a keto recipe?')
    upload_recipe = SubmitField('Upload Recipe')
