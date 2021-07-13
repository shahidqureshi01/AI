from users import User
from db import db_engine
from sqlalchemy.orm import Session

engine = db_engine()
session = Session(engine, True)
user = User(name='Ubeyt',last_name='Demir',email='ubeytdemir4se@gmail.com', id=20, password_hash='test')
session.add(user)
session.commit()

user2 = session.query(User).get(20)
