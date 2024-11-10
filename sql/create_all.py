import os
from sqlalchemy import create_engine, MetaData
from model import db
from dotenv import load_dotenv

load_dotenv()
database_uri = os.getenv('DATABASE_URI')
engine = create_engine(database_uri, echo=True)

metadata = MetaData()

metadata.reflect(bind=engine)

db.create_all(bind=engine, tables=[table for table in metadata.sorted_tables])
