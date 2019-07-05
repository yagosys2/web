from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[
        DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired()])
    confirm_password = PasswordField('Confirm  password', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[
        DataRequired()])
    submit = SubmitField('Login')


class SearchForm(FlaskForm):
    isbn = StringField('isbn', validators=[
        DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Search')
