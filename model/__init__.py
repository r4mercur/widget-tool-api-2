__all__ = ['db', 'general', 'liveticker', 'match', 'team', 'competion']

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
db = SQLAlchemy()
