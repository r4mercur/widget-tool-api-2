from sqlalchemy import create_engine, MetaData
from model import db

engine = create_engine('mysql://root:root@localhost:3306/dfbnet', echo=True)

metadata = MetaData()

metadata.reflect(bind=engine)

db.create_all(bind=engine, tables=[table for table in metadata.sorted_tables])
