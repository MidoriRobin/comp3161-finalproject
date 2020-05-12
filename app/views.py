#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from app import app, db, login_manager
from flask import Flask, render_template, request, redirect, url_for, flash
from app.classes import *
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from .forms import *
import os
from sqlalchemy import bindparam
from sqlalchemy.sql import text
from flask_login import login_user, logout_user, current_user, login_required

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

#app = Flask(__name__)
#app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('layouts/dash.html')


@app.route('/about')
def about():

    with db.connect() as conn:
        s = text("SELECT * FROM usr")
        result = conn.execute(s)
        print(result.fetchone())

    return render_template('pages/placeholder.about.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    #form = LoginForm(request.form)
    form = LoginForm()

    if request.method == 'POST':
        if form.name.data:
            email = form.name.data

            print("Printing verification")
            print(verify_user(email))
            id, lname, fname, email, date, password = verify_user(email)
            user = User(id, fname, lname)
            print(user)

            if user is not None:
                login_user(user)
                flash('User logged in successfully!', 'success')
                print("success!")

            return redirect(url_for('about'))
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

@app.route('/profile')
def profile():
    return render_template('layouts/profile.html')

@app.route('/admin')
def admin():
    return render_template('layouts/admin.html')

@app.route('/edit')
def edit():
    return render_template('layouts/editprofile.html')

@app.route('/post')
def post():
    return render_template('layouts/post.html')


    #render the page with the selected post using the post id


def verify_user(email, passw=None):
    print("verifying user..")

    if passw == None:
        with db.connect() as conn:
            stmt = text("SELECT * FROM usr WHERE usr.email LIKE :e")
            stmt.bindparams(bindparam("e", type_=str))
            result = conn.execute(stmt, {"e": email})


    elif passw != None:
        with db.connect() as conn:
            stmt = text("SELECT * FROM usr WHERE usr.email LIKE :e AND usr.password LIKE :passw")
            stmt.bindparams(bindparam("e", type_=str),bindparam("passw", type_=str))
            result = conn.execute(stmt, {"e": email, "passw": passw})
            print("Done")
    else:
        result = None
        print("Done")

    print("verification complete!")
    #print("Result is: %s", result.fetchone())
    return result.fetchone()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
