from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from . import db 
from . import login_manager




class User(UserMixin,db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref = 'user',lazy = True)
    comments = db.relationship('Comment',backref = 'user',lazy = True)
  

    @login_manager.user_loader
    def load_user(user_id):
         return User.query.get(int(user_id))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


    # @property
    # def password(self):
    #     raise AttributeError('You cannot read the password')

    # @password.setter
    # def password(self,password):
    #     self.pass_secure = generate_password_hash(password)

    
    # def verify_password(self,password):
    #     return check_password_hash(self.pass_secure,password)

    # def __repr__(self):
    #     return f'User{self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key=True)
    #user_id = db.Column(db.Integer,db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(255),index = True)
    description = db.Column(db.String(255),index = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"), nullable=False)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"), nullable=False)
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))


# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User',backref = 'role',lazy="dynamic")
#     pass_secure = db.Column(db.String(255))
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"), nullable=False)
#     blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
#     comments_id = db.Column(db.Integer,db.ForeignKey("comments.id"))

    def __repr__(self):
        return f'User {self.name}'

class Quote:
    def __init__(self,author,quote):
        #self.id = id
        self.author = author
        self.quote = quote

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))