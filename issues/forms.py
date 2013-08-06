from flask.ext.wtf import Form, TextField, PasswordField, validators


class AddUserForm(Form):
    email = TextField('Email address', [validators.Required(message='Email is required'), validators.Email(message='Invalid email address')])
    name = TextField('Name', [validators.Required(message='Name is required')])
    password = PasswordField('Password', [validators.Required(message='Password is required'), validators.EqualTo('confirm', message='Passwords do not match')])
    confirm  = PasswordField('Repeat Password')