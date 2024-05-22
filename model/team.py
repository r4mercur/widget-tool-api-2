from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from utils import autoserialize
from model import db


class TeamType(db.Model, autoserialize.AutoSerialize):
    __name__ = 'TeamType'
    __public__ = ('id', 'name')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(255))


class Team(db.Model, autoserialize.AutoSerialize):
    __name__ = 'Team'
    __public__ = ('id', 'name')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(100))
    fkSportType = db.Column(BIGINT, db.ForeignKey('SportType.id'))
    fkTeamType = db.Column(BIGINT, db.ForeignKey('TeamType.id'))
    sportType = db.relationship('SportType', foreign_keys='Team.fkSportType', lazy='joined')
    teamType = db.relationship('TeamType', foreign_keys='Team.fkTeamType', lazy='joined')


class Player(db.Model, autoserialize.AutoSerialize):
    __name__ = 'Player'
    __public__ = ('id', 'firstName', 'lastName')
    id = db.Column(BIGINT, primary_key=True)
    firstName = db.Column(VARCHAR(100))
    lastName = db.Column(VARCHAR(100))
