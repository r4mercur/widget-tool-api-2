from sqlalchemy.dialects.mysql import BIT, BIGINT, DATE, DATETIME, TEXT, TINYINT, CHAR, VARCHAR, DOUBLE, LONGBLOB, LONGTEXT
from autoserialize import AutoSerialize
from model import db

class ResultCode(db.Model, AutoSerialize):
    __name__ = 'ResultCode'
    __public__ = ('id', 'name', 'shortName')
    id = db.Column('id', BIGINT, primary_key=True)
    name = db.Column('name', VARCHAR(100))
    shortName = db.Column('shortName', VARCHAR(100))

class Match(db.Model, AutoSerialize):
    __name__ = 'Match'
    __public__ = ('id', 'fkCompetion')
    id = db.Column('id', BIGINT, primary_key=True)
    fkCompetion = db.Column(BIGINT, db.ForeignKey('Competion.id'))
    fkSeason = db.Column(BIGINT, db.ForeignKey('Season.id'))
    fkTeamHome = db.Column(BIGINT, db.ForeignKey('Team.id'))
    fkTeamAway = db.Column(BIGINT, db.ForeignKey('Team.id'))
    fkResultCode = db.Column(BIGINT, db.ForeignKey('ResultCode.id'))
    goalsHome = db.Column(BIGINT)
    goalsAway = db.Column(BIGINT)
    goalsAgainstHome = db.Column(BIGINT)
    goalsAgainstAway = db.Column(BIGINT)
    goalsHomeHalftime = db.Column(BIGINT)
    goalsAwayHalftime = db.Column(BIGINT)
    matchDate = db.Column(DATETIME)
    matchDay = db.Column(BIGINT)
    location = db.Column(VARCHAR(200))
    referee = db.Column(VARCHAR(100))
    visitors = db.Column(BIGINT)
    liveGoalsHome = db.Column(BIGINT)
    liveGoalsAway = db.Column(BIGINT)

class Goal(db.Model, AutoSerialize):
    __name__ = 'Goal'
    __public__ = ('id', 'fkMatch', 'fkPlayer', 'fkTeam', 'minute', 'penalty', 'ownGoal')
    id = db.Column('id', BIGINT, primary_key=True)
    fkMatch = db.Column(BIGINT, db.ForeignKey('Match.id'))
    fkPlayer = db.Column(BIGINT, db.ForeignKey('Player.id'))
    fkTeam = db.Column(BIGINT, db.ForeignKey('Team.id'))
    minute = db.Column(BIGINT)
    penalty = db.Column(BIT)
    ownGoal = db.Column(BIT)