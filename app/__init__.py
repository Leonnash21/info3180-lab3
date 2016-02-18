import os
from flask import Flask
from flask.ext.sendmail import Mail

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField

app = Flask(__name__)
from app import views


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['DEFAULT_MAIL_SUBJECT'] = '[User def]'
app.config['DEFAULT_MAIL_SENDER'] = 'Admin <admin@example.com>'
app.config['SECRET_KEY'] = 'random_string'
app.config['DEFAULT_ADMIN'] = 'Admin <admin@example.com>'

mail = Mail(app)

class Contact(Form):
    name = StringField('Enter name')
    submit = SubmitField('Submit')
