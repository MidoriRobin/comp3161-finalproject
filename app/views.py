#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from app import app, db, login_manager
from flask import Flask, render_template, request, redirect, g, url_for, flash, session
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
    posts = None
    user = 323493

    posts = fetch_curr_usr_pst(user)

    #print(results)
    return render_template('layouts/dash.html', posts=posts, user=user)


@app.route('/about')
def about():
    # userid = 323493
    # postid = 1
    # numPost = 0
    # txtPost = []
    # phPost = []
    #
    # fetch_curr_usr_pst(userid)

    #t_posts, p_posts=fetch_all_posts()
    # print("Text posts \n")
    # print(t_posts)
    # print("Photo posts \n")
    # print(p_posts)

    return render_template('pages/placeholder.about.html', t_posts=t_posts, p_posts=p_posts)


@app.route('/login', methods=["GET", "POST"])
def login():
    #form = LoginForm(request.form)
    form = LoginForm()

    if request.method == 'POST':
        print("Post requested")
        if (request.form['email']):
            email = request.form['email']

            print("Printing verification")
            print(verify_user(email))
            id, lname, fname, email, date, password = verify_user(email)
            user = User( lname, fname, email, uid=id)
            print(user)

            if user is not None:
                login_user(user)
                session['uid'] = user.uid
                session['logged_in'] = True
                print("Logged in")
                g.current_user = user
                flash('User logged in successfully!', 'success')
                print("success!")

                return redirect(url_for('home'))
        else:
            print("No such usr")

    return render_template('forms/login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('uid', None)
    logout_user()
    flash('You were logged out', 'success')
    return redirect(url_for('home'))


@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        uname = request.form['username']
        birth = request.form['DOB']
        email = request.form['email']
        password = request.form['password']

        user = User(lname, fname, email, uname=uname, password=password, birth=birth)
        print(user)

    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)


@app.route('/profile/<user_id>', methods=['GET'])
def profile(user_id):

    empty = ''
    print(user_id)
    #userid = 323493

    with db.connect() as conn:
        stmt = text("SELECT fname, lname, email, dob, bio, u_name, num_of_friends FROM usr "
                "JOIN register ON usr.u_id=register.u_id "
                "JOIN prfl ON register.p_id=prfl.p_id "
                "WHERE usr.u_id = :uid ")
        stmt.bindparams(bindparam("uid", type_=str))
        results = conn.execute(stmt, {"uid": user_id})

        result = results.fetchone()

    print(result)

    return render_template('layouts/profile.html', result=result, posts=empty)


@app.route('/admin', methods=["GET","POST"])
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


    #render the page with the selected post using the post id

def fetch_all_posts():
    txtPosts = []
    phtPosts = []
    pList = []

    with db.connect() as conn:
        t_stmt = text("SELECT p_text.*, datePosted FROM p_text "
                "JOIN generates ON p_text.post_id=generates.post_id "
                "ORDER BY datePosted "
                "LIMIT 10 ")

        p_stmt = text("SELECT photo.*, datePosted FROM photo "
                "JOIN generates ON photo.post_id=generates.post_id "
                "ORDER BY datePosted "
                "LIMIT 10 ")

        t_results = conn.execute(t_stmt)
        p_results = conn.execute(p_stmt)
        #print(results)

        txtPost = t_results.fetchall()
        phtPost = p_results.fetchall()

        print(txtPost)


    return (txtPost,phtPost)

def fetch_curr_usr_pst(userid):

    with db.connect() as conn:
        stmt = text("SELECT post.post_id FROM usr "
                "JOIN generates ON usr.u_id=generates.u_id "
                "JOIN post ON generates.post_id=post.post_id "
                "WHERE usr.u_id = :uid ")
        stmt.bindparams(bindparam("uid", type_=str))
        results = conn.execute(stmt, {"uid": userid})
        numPost = len([result.values()[0] for result in results.fetchall()])
        print(numPost)

    if numPost == 0:
        print("User has made no posts")
    else:
        with  db.connect() as connection:
            nconn = connection.connection
            cursor = nconn.cursor()
            cursor.callproc("GetTextPosts", [userid])
            t_results = cursor.fetchall()
            cursor.close()
            nconn.commit()
        numPost -= len(t_results)

        if numPost != 0:
            with  db.connect() as connection:
                nconn = connection.connection
                cursor = nconn.cursor()
                cursor.callproc("GetPhotoPosts", [userid])
                p_results = cursor.fetchall()
                cursor.close()
                nconn.commit()
            numPost -= len(p_results)

        print(t_results)

        posts = [Post(result[0], result[4], result[5], result[3], result[1]) for result in t_results]

        print(posts)

    return posts

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
