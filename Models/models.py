#from app import db
from flask_sqlalchemy import SQLAlchemy
#from Models.ModelMixins import ModelMixin
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from Models.ModelMixins import ModelMixins
from flask_user import login_required, UserManager, UserMixin
from extensiondb import db
from flask_bcrypt import generate_password_hash, check_password_hash


Base = declarative_base()


class ProductLst(db.Model, ModelMixins,UserMixin):
    sno = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(200),nullable=False)
    Price = db.Column(db.Integer,nullable=False)

    def to_dict(self):
        tempdict = {"sno": self.sno, "Name": self.Name, "Price": self.Price}
        return tempdict


class Token(db.Model, ModelMixins):
    sno = db.Column(db.Integer,db.ForeignKey('users.sno', ondelete='CASCADE'), primary_key=True, nullable=False,)
    token= db.Column(db.String, nullable=False)


class Users(db.Model, ModelMixins):
    #__tablename__ = 'users'
    sno = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    permission = db.Column(db.Integer,nullable=False)
    token = db.relationship('Token',backref='my_token')

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        tempdict = {"sno":self.sno,"Name":self.Name,"Password":self.password,"permission":self.permission}
        return tempdict