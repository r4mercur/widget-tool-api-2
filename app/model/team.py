from sqlalchemy.dialects.mysql import BIT, BIGINT, DATE, DATETIME, TEXT, TINYINT, CHAR, VARCHAR, DOUBLE, LONGBLOB, LONGTEXT
from autoserialize import AutoSerialize
from model import db

class TeamType(db.Model, AutoSerialize):
    __tablename__ = 'TeamType'
    __public__ = ('id', 'name')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(255))

class Team(db.Model, AutoSerialize):
    __tablename__ = 'Team'
    __public__ = ('id', 'name')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(100))
    fkSportType = db.Column(BIGINT, db.ForeignKey('SportType.id'))
    fkTeamType = db.Column(BIGINT, db.ForeignKey('TeamType.id'))
    sportType = db.relationship('SportType', foreign_keys='Team.fkSportType', lazy='joined')
    teamType = db.relationship('TeamType', foreign_keys='Team.fkTeamType', lazy='joined')

class Player(db.Model, AutoSerialize):
    __tablename__ = 'Player'
    __public__ = ('id', 'firstName', 'lastName')
    id = db.Column(BIGINT, primary_key=True)
    firstName = db.Column(VARCHAR(100))
    lastName = db.Column(VARCHAR(100))
