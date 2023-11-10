from sqlalchemy.dialects.mysql import BIT, BIGINT, DATE, DATETIME, TEXT, TINYINT, CHAR, VARCHAR, DOUBLE, LONGBLOB, LONGTEXT
from autoserialize import AutoSerialize
from model import db

class Season(db.Model, AutoSerialize):
    __tablename__ = 'Season'
    __public__ = ('id', 'name', 'current', 'year')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(100))
    current = db.Column(BIT)
    year = db.Column(BIGINT)
    dfbNetKey = db.Column(VARCHAR(20))

class CompetionType(db.Model, AutoSerialize):
    __tablename__ = 'CompetionType'
    __public__ = ('id', 'name')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(255))
    fkGender = db.Column(BIGINT, db.ForeignKey('Gender.id'))
    gender = db.relationship('Gender', foreign_keys='CompetionType.fkGender', lazy='joined')

class Competion(db.Model, AutoSerialize):
    __tablename__ = 'Competion'
    __public__ = ('id', 'name', 'shortName')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(255))
    shortName = db.Column(VARCHAR(100))
    fkCompetionType = db.Column(BIGINT, db.ForeignKey('CompetionType.id'))
    competionType = db.relationship('CompetionType', foreign_keys='Competion.fkCompetionType', lazy='joined')

class CompetionRound(db.Model, AutoSerialize):
    __tablename__ = 'CompetionRound'
    __public__ = ('id', 'name')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(255))
    fkCompetion = db.Column(BIGINT, db.ForeignKey('Competion.id'))
    competion = db.relationship('Competion', foreign_keys='CompetionRound.fkCompetion', lazy='joined')
    count = db.Column(BIGINT)

class CompetionGroup(db.Model, AutoSerialize):
    __tablename__ = 'CompetionGroup'
    __public__ = ('id', 'name')
    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(VARCHAR(255))
    fkCompetionRound = db.Column(BIGINT, db.ForeignKey('CompetionRound.id'))
    competionRound = db.relationship('CompetionRound', foreign_keys='CompetionGroup.fkCompetionRound', lazy='joined')

class PublisherCompetionMap(db.Model, AutoSerialize):
    __tablename__ = 'PublisherCompetionMap'
    __public__ = ('id', 'fkPublisher', 'fkCompetion')
    id = db.Column(BIGINT, primary_key=True)
    fkPublisher = db.Column(BIGINT, db.ForeignKey('Publisher.id'))
    publisher = db.relationship('Publisher', foreign_keys='PublisherCompetionMap.fkPublisher', lazy='joined')
    fkCompetion = db.Column(BIGINT, db.ForeignKey('Competion.id'))
    competion = db.relationship('Competion', foreign_keys='PublisherCompetionMap.fkCompetion', lazy='joined')

class CompetionSeasonMap(db.Model, AutoSerialize):
    __tablename__ = 'CompetionSeasonMap'
    __public__ = ('id', 'fkCompetion', 'fkSeason', 'placesPromotion', 'placesPromotionExpul', 'placesRelegation', 'placesRelegationExpul')
    id = db.Column(BIGINT, primary_key=True)
    fkCompetion = db.Column(BIGINT, db.ForeignKey('Competion.id'))
    competion = db.relationship('Competion', foreign_keys='CompetionSeasonMap.fkCompetion', lazy='joined')
    fkSeason = db.Column(BIGINT, db.ForeignKey('Season.id'))
    season = db.relationship('Season', foreign_keys='CompetionSeasonMap.fkSeason', lazy='joined')
    placesPromotion = db.Column(TINYINT)
    placesPromotionExpul = db.Column(TINYINT)
    placesRelegation = db.Column(TINYINT)
    placesRelegationExpul = db.Column(TINYINT)

class CompetionTeamMap(db.Model, AutoSerialize):
    __tablename__ = 'CompetionTeamMap'
    __public__ = ('id', 'fkCompetion', 'fkTeam', 'fkSeason')
    id = db.Column(BIGINT, primary_key=True)
    fkCompetion = db.Column(BIGINT, db.ForeignKey('Competion.id'))
    competion = db.relationship('Competion', foreign_keys='CompetionTeamMap.fkCompetion', lazy='joined')
    fkTeam = db.Column(BIGINT, db.ForeignKey('Team.id'))
    team = db.relationship('Team', foreign_keys='CompetionTeamMap.fkTeam', lazy='joined')
    fkSeason = db.Column(BIGINT, db.ForeignKey('Season.id'))
    season = db.relationship('Season', foreign_keys='CompetionTeamMap.fkSeason', lazy='joined')
