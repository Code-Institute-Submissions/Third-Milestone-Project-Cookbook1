from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField
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
    image = StringField('Insert Image Link (full url)', [
                               validators.InputRequired()])
    recipe_title = StringField('Recipe Title', [
                               validators.InputRequired(),
                               validators.Length(min=4, max=85)])
    recipe_story = TextAreaField('Add a short story...', [
                                 validators.DataRequired(),
                                 validators.Length(min=5, max=200)])
    ingredients = StringField('Add ingredients by line', [
                              validators.InputRequired()])
    steps = TextAreaField('Step by step method', [
                          validators.DataRequired(),
                          validators.Length(min=5, max=1300)])
    categories = SelectField('Recipe category (Please select at least one)',
                             choices=[('breakfast', 'Breakfast'),
                                      ('main', 'Main Meal'),
                                      ('snacks', 'Snacks')])
    keto_recipes = BooleanField('Is this a keto recipe?')
    upload_recipe = SubmitField('Upload Recipe')


class EditProfileForm(FlaskForm):
    profile_img = StringField('Profile Picture', [
                            validators.InputRequired()])
    save_profile = SubmitField('Save')


class EditRecipeForm(FlaskForm):
    image = StringField('Insert Image Link (full url)', [
                               validators.InputRequired()])
    recipe_title = StringField('Recipe Title', [
                               validators.InputRequired(),
                               validators.Length(min=4, max=85)])
    recipe_story = TextAreaField('Add a short story...', [
                                 validators.DataRequired(),
                                 validators.Length(min=5, max=200)])
    ingredients = StringField('Add ingredients by line', [
                              validators.InputRequired()])
    steps = TextAreaField('Step by step method', [
                          validators.DataRequired(),
                          validators.Length(min=5, max=1300)])
    categories = SelectField('Recipe category (Please select at least one)',
                             choices=[('breakfast', 'Breakfast'),
                                      ('main', 'Main Meal'),
                                      ('snacks', 'Snacks')])
    keto_recipes = BooleanField('Is this a keto recipe?')
    save_recipe = SubmitField('Save Changes')
