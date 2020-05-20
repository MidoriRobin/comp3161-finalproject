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
from datetime import date

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('layouts/dash.html')

@app.route('/firstpage')
def firstpage():
    return render_template('layouts/first.html')


@app.route('/about')
def about():

    """with db.connect() as conn:
        s = text("SELECT * FROM `usr`"
        "WHERE u_id BETWEEN 100000 AND 200000")
        result = conn.execute(s)
        print(result.fetchmany(5))"""

    with  db.connect() as connection:
        nconn = connection.connection
        cursor = nconn.cursor()
        cursor.callproc("GetPostComments", ['1'])
        results = list(cursor.fetchall())
        cursor.close()
        nconn.commit()

    print(results)

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

@app.route('/admin', methods=["GET"])
def admin():
    usrttl = 0
    pstttl = 0
    txtttl = 0
    pttl = 0
    metric = []

    with db.connect() as conn:
        stmt1 = text("SELECT COUNT(u_id) from usr")
        stmt2 = text("SELECT COUNT(post_id) from post")
        stmt3 =text("SELECT COUNT(photo_id) from photo;")
        stmt4 =text("SELECT COUNT(t_id) from p_text")

        stList = [stmt1,stmt2,stmt3,stmt4]

        for stmt in stList:
            result =conn.execute(stmt)
            metric.append(result.fetchone())
        print(metric)

    return render_template('layouts/admin.html', metrics=metric)

@app.route('/admin/<userName>', methods=["GET","POST"])
def show_user(userName):

    with db.connect() as conn:
        stmt = text("SELECT usr.* FROM `usr` "
        "JOIN register ON usr.u_id=register.u_id "
        "JOIN prfl ON register.p_id=prfl.p_id "
        "WHERE prfl.u_name LIKE :uname")
        stmt.bindparams(bindparam("uname", type_=str))
        result = conn.execute(stmt, {"uname": userName})
        userArrays = result.fetchall()
    print(len(userArrays))

    users = []

    for user in userArrays:
        id, lname, fname, email, dobirth, passw = user
        nUser = User(id, lname, fname, email, birth=dobirth)
        users.append(nUser)

    return render_template('layouts/admin-user.html', Users=users)


@app.route('/edit')
def edit():
    return render_template('layouts/editprofile.html')

@app.route('/post')
def post():
    return render_template('layouts/post.html')

@app.route('/groups')
def group():
    return render_template('layouts/group.html')


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
            stmt = text("SELECT * FROM usr WHERE usr.email"
            "LIKE :e AND usr.password LIKE :passw")
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
