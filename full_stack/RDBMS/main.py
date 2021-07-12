from db import db_engine
from sqlalchemy.orm import Session

engine = db_engine()
session = Session(engine, future=True)