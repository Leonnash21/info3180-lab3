"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
import cgi
import smtplib
<<<<<<< HEAD
from flask.ext.sendmail import Message 
import os

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
=======

>>>>>>> 3f7944126be42ccc3e27a2b2c49d2b6ad627b65f

###
# Routing for your application.
###

<<<<<<< HEAD


def sendemail(to, subject, template, **kwargs):
    msg=Message(app.config['DEFAULT_MAIL_SUBJECT']+''+ subject, sender=app.config['DEFAULT_MAIL_SENDER'],recipients=[to])
    msg.html = render_template(template + '.html', **kwargs) 
    mail.sendmail(msg)



@app.route('/send', methods = ('GET', 'POST'))
def submit():
    form = contact()
    if form.validate_on_submit():
        name = form.name.data
        send_email(app.config['DEFAULT_ADMIN'], 'Button clicked', 'mail/', Fullname=name)
        return redirect('/send')
    return render_template('index.html', form=form)
    
    
=======
>>>>>>> 3f7944126be42ccc3e27a2b2c49d2b6ad627b65f

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
    
@app.route('/contact')
def contact ():
    """shows contact page"""
    return render_template('contact.html')
    





if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
