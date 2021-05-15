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
    image = FileField('Choose Image', [validators.DataRequired()]),
    upload_img = SubmitField('Upload File'),
    recipe_title = StringField('Recipe Title', [
                               validators.InputRequired(),
                               validators.Length(min=4, max=45)])
    recipe_story = TextAreaField('Add a short story...', [
                                 validators.DataRequired(),
                                 validators.Length(min=5, max=200)])
    ingredients = StringField('Add ingredients by line', [
                              validators.InputRequired()])
    steps = TextAreaField('Step by step method', [
                          validators.DataRequired(),
                          validators.Length(min=5, max=260)])
    categories = SelectMultipleField('Recipe category (PLease select at least one)',
                                     choices=[('Breakfast', 'breakfast'),
                                              ('Main meal', 'main'),
                                              ('Snacks', 'snacks')])
    keto_recipes = BooleanField('Is this a keto recipe?')
    upload_recipe = SubmitField('Upload Recipe')


class EditProfileForm(FlaskForm):
    profile_img = FileField('Profile Picture', [
                            validators.InputRequired()])
    user_bio = TextAreaField('Add Bio',
                             [validators.InputRequired(),
                              validators.Length(min=5, max=250)])
    save_profile = SubmitField('Save')


class EditRecipeForm(FlaskForm):
    edit_image = FileField('Choose Image', [validators.DataRequired()]),
    edit_recipeimg = SubmitField('Upload File'),
    edit_recipe_title = StringField('Recipe Title', [
        validators.InputRequired(),
        validators.Length(min=4, max=45)])
    edit_recipe_story = TextAreaField('Add a short story...', [
        validators.DataRequired(),
        validators.Length(min=5, max=200)])
    edit_ingredients = StringField('Add ingredients by line', [
        validators.InputRequired()])
    edit_steps = TextAreaField('Step by step method', [
        validators.DataRequired(),
        validators.Length(min=5, max=260)])
    edit_categories = SelectMultipleField('Recipe category (PLease select at least one)',
                                          choices=[('Breakfast', 'breakfast'),
                                                   ('Main meal', 'main'),
                                                   ('Snacks', 'snacks')])
    edit_keto_recipes = BooleanField('Is this a keto recipe?')
    save_recipe = SubmitField('Save Changes')
