from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
# from sqlalchemy import Column, Integer, String
from app import db
from sqlalchemy import bindparam
from sqlalchemy.sql import text
import datetime

#engine = create_engine('sqlite:///database.db', echo=True)
#db_session = scoped_session(sessionmaker(autocommit=False,
#                                         autoflush=False,
#                                         bind=engine))
#Base = declarative_base()
#Base.query = db_session.query_property()

# Set your classes here.

class User(UserMixin):
    """docstring for User."""

    def __init__(self, lname, fname, email, uid=None, uname=None, password=None, birth=None):
        self.uid = uid
        self.username = uname
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.age = None
        self.DOB = birth
        self.password = password


    # Might not be necessary here, better placed in comment class?
    def get_comment(self, postid):
        pass

    # Needs an update query
    def set_uname(self, newname):
        """This allows for the rewriting of the username of the user.

            Allows the user to change their username and carries over all changes
            from the front end to the database.
        """

        self.username = newname

        with db.connect() as conn:
            # The SQL query goes in the text functon below
            # stmt = text()
            stmt.bindparams(bindparam("name", type_=str))
            result = conn.execute()
        pass

    # Also needs an update query
    def set_pass(self, pname):
        """This allows for the rewriting of the passoword of the user.

            Allows the user to change their passoword and carries over all changes
            from the front end to the database.
        """

        self.password = pname

        with db.connect() as conn:
            # The SQL query goes in the text functon below
            # stmt = text()
            stmt.bindparams(bindparam("pass", type_=str))
            result = conn.execute()
        pass

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.uid)  # python 2 support
        except NameError:
            return str(self.uid)  # python 3 support

    @staticmethod
    def get(id):
        with db.connect() as conn:
            stmt = text("SELECT * FROM usr WHERE usr.u_id LIKE :id")
            stmt.bindparams(bindparam("id", type_=str))
            result = conn.execute(stmt, {"id": id})

        return result.fetchone()

    def __repr__(self):
        return '<User: %r,%r,%r,%r,%r,%r>' % (self.firstname, self.lastname, self.username, self.DOB, self.email, self.password)


class Profile():
    """docstring for Profile: An object to store users information regarding their Profile

        """

    def __init__(self, p_id, uname, p_pic, bio, u_name, num_of_friends):
        super(Profile, self).__init__()

        self.profileId = p_id
        self.username = uname
        self.profilePic = p_pic
        self.biography = bio
        self.userName = u_name
        self.NoF = num_of_friends

    def set_picture(self, picture):
        """Allows the user to reset their profile picture.

            Changes the profile picture of the user
            and carries over all changes to the database
        """

        pass

    def inc_friend(self, arg):
        self.NoF = self.NoF + 1

    def edit_bio(self, about):
        self.biography = about

    def set_uname(self, nname):
        """This allows for the rewriting of the username of the user.

            Allows the user to change their username and carries over all changes
            from the front end to the database.
        """

        pass

    def mname(self, arg):
        pass


class Admin(User):
    """docstring for Admin."""

    def __init__(self):
        super(Admin, self).__init__()

    def fetch_all_users(self, datejoined, firstname=None, lastname=None):

        pass

        #if name == None:
        #    #A "Select *" query would go here
        #    pass
        #elif:
        #    pass

    def fetch_by_date(self, date, User=True, Posts=False):
        with db.connect() as conn:
            s = text("SELECT `u_id`, `lname`, `fname` FROM `usr`"
            "WHERE u_id BETWEEN 100000 AND 200000")
            result = conn.execute(s)
        pass

    def fetch_by_lname(self, lname):

        with db.connect() as conn:
            s = text("SELECT * FROM `usr`"
            "WHERE u_id BETWEEN 100000 AND 200000")
            result = conn.execute(s)
        pass

    def fetch_by_fname(self, fname):
        pass

    def fetch_by_uname(self, arg):
        pass

    def fetch_all_posts(self, arg):
        pass


class FrontUser(User):
    """docstring for FrontUser."""

    def __init__(self, dob, datejoined):
        super(FrontUser, self).__init__()
        self.dob = dob
        self.joindate = datejoined
        self.postLst = []

    def view_friends(self):
        """Allows user to view all friends

            Makes a query to the database and fetches a list of friends,
            listing only ID and First and Last name
        """
        with db.connect() as conn:
            # The SQL query goes in the text functon below
            # stmt = text()
            stmt.bindparams(bindparam("id", type_=str))
            result = conn.execute()
        pass

    def add_friend(self, friendid):
        """Allows the user to add another user to thier friends list

            Adds another user to this user's list of friends,
            also makes a SQL insert, so changes are maintained on the database
        """

        with db.connect() as conn:
            # The SQL query goes in the text functon below
            # stmt = text()
            stmt.bindparams(bindparam("id", type_=str))
            result = conn.execute()
        pass

    def fetch_posts(self):
        """This fuction retrieves posts from the database.

            Using mySQL syntax, retrieves all the posts made by this user and stores
            them in an array.
        """
        with db.connect() as conn:
            # The SQL query goes in the text functon below
            # stmt = text()
            stmt.bindparams(bindparam("id", type_=str))
            result = conn.execute()
        return

    def add_post(self, content, datemade):
        """Allows the user to create a new post, and adds it to their list of posts.

            Upon creation of a new post, this post is added to the database
            via an insert statement, so changes are reflected
        """
        with db.connect() as conn:
            # The SQL query goes in the text functon below
            # stmt = text()
            stmt.bindparams(bindparam("id", type_=str))
            result = conn.execute()
        pass

    def get_comments(self):
        """This function fetches every comment ever made by the user

        Using mySQL syntax fetches all comments made by the user on the database
        and stores them in an array
        """
        pass


class Post():
    """docstring for Post."""

    def __init__(self, uid, content, date, pid=None, likes=0, comments=[]):

        self.pid = pid
        self.uid = uid
        self.content = content
        self.date = date
        self.commentLst = comments
        self.likes = likes

    def view_comments(self):

        with db.connect() as conn:
            # The SQL query goes in the text functon below
            # stmt = text()
            stmt.bindparams(bindparam("id", type_=str))
            result = conn.execute()
        pass

    def incr_likes(self):

        with db.connect() as conn:
            # The SQL query goes in the text functon below
            # stmt = text()
            stmt.bindparams(bindparam("id", type_=str))
            result = conn.execute()

        self.likes += 1

    def add_comment(self, pid, uid, comment, date):
        return comments.append(comment(pid,uid,comment,date))

    def type(self, arg):

        if pid == None:
            Type = "Photo"
        else:
            Type = "Text"

        return Type
            
    def __repr__(self):
        return '<PostID: %r>' %  self.pid

class BlogGroup(object):
    """docstring for BlogGroup."""

    def __init__(self, name, posts, bid=None, members=None):
        super(BlogGroup, self).__init__()
        self.bid = bid
        self.bname = name
        self.members = members
        self.bposts = posts

    def list_members(self):
        """Lists all the members in this blog group"""
        pass

    def list_posts(self):

        with db.connect() as conn:
            # The SQL query goes in the text functon below
            # stmt = text()
            stmt.bindparams(bindparam("id", type_=str))
            result = conn.execute()
        pass

    def add_editor(self, arg):
        pass

    def add_member(self, arg):
        pass

    def add_post(self, arg):
        pass


class Profile():
    """docstring for Profile."""

    def __init__(self, arg):
        super(Profile, self).__init__()
        self.arg = arg


class Comment():
    """docstring for Comment."""

    def __init__(self, postid, uid, content, dateMade):
        super(Comment, self).__init__()
        self.postID = postid
        self.uId = uid
        self.content = content
        self.date = dateMade

    def mname(self, arg):
        pass





# Create tables.
