from sqlalchemy.dialects.mysql import BIT, BIGINT, DATETIME, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from utils import autoserialize
from model import db

Base = declarative_base()

class Gender(db.Model, autoserialize.AutoSerialize, Base):
    __name__ = 'Gender'
    __public__ = ('id', 'name')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(100))


class Publisher(db.Model, autoserialize.AutoSerialize, Base):
    __name__ = 'Publisher'
    __public__ = ('id', 'name', 'description', 'domain', 'mail')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(100))
    description = db.Column(VARCHAR(1000))
    domain = db.Column(VARCHAR(100))
    mail = db.Column(VARCHAR(50))


class User(db.Model, autoserialize.AutoSerialize, Base):
    __name__ = 'User'
    __public__ = (
        'id', 'firstName', 'lastName', 'email', 'password', 'authToken', 'admin', 'registrationDate', 'lastLoginDate')
    id = db.Column(BIGINT, primary_key=True)
    firstName = db.Column(VARCHAR(100))
    lastName = db.Column(VARCHAR(100))
    email = db.Column(VARCHAR(100))
    password = db.Column(VARCHAR(128))
    authToken = db.Column(VARCHAR(256))
    admin = db.Column(BIT)
    registrationDate = db.Column(DATETIME)
    lastLoginDate = db.Column(DATETIME)
    fkPublisher = db.Column(BIGINT, db.ForeignKey('Publisher.id'))
    publisher = relationship('Publisher', back_populates='users')


class SportType(db.Model, autoserialize.AutoSerialize, Base):
    __name__ = 'SportType'
    __public__ = ('id', 'name')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(255))
