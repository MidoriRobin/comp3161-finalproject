from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# from app import db

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.

'''
class User(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
'''

class User():
    """docstring for User."""

    def __init__(self, uid=None, uname, fname, lname, birth, pword):
        self.uid = uid
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.DOB = birth
        self.password = password
        self.datejoined = joined

    def get_posts(self):
        """This fuction retrieves posts from the database

        Using mySQL syntax, retrieves all the posts made by this user and stores
        them in an array
        """
        pass

    def get_comments(self):
        """This function fetches every comment ever made by the user

        Using mySQL syntax fetches all comments made by the user on the database
        and stores them in an array
        """
        pass

    def get_comment(self, postid):
        pass

    def set_uname(self, nname):
        pass

    def set_pass(self, pname):
        pass


class Admin(User):
    """docstring for Admin."""

    def __init__(self):
        super(Admin, self).__init__()

    def fetch_all_users(self, firstname=None, lastname=None, datejoined):

        if name == None:
            #A "Select *" query would go here
            pass
        elif :
        pass

    def fetch_by_date(self, date):
        pass

    def fetch_by_lname(self, arg):
        pass

    def fetch_by_fname(self, arg):
        pass

    def fetch_all_posts(self, arg):
        pass


class FrontUser(User):
    """docstring for FrontUser."""

    def __init__(self, arg):
        super(FrontUser, self).__init__()
        self.arg = arg


class Posts():
    """docstring for Posts."""

    def __init__(self, pid=None, uid, content, date):

        self.pid = pid
        self.uid = uid
        self.content = content
        self.date = date



class BlogGroup(object):
    """docstring for BlogGroup."""

    def __init__(self, bid=None, name, members=None, posts):
        super(BlogGroup, self).__init__()
        self.bid = bid
        self.bname = name
        self.members = members
        self.bposts = posts

    def list_members(self):
        """Lists all the members in this blog group"""
        pass

    def list_posts(self):
        pass

    def add_editor(self, arg):
        pass

    def add_member(self, arg):
        pass


class Profile():
    """docstring for Profile."""

    def __init__(self, arg):
        super(Profile, self).__init__()
        self.arg = arg



# Create tables.
