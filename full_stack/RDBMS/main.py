from users import User
from db import db_engine
from sqlalchemy.orm import Session

engine = db_engine()
session = Session(engine, True)
user = User(name='Ubeyt',last_name='Demir',email='ubeytdemir4se@gmail.com', id=43, password_hash='test')
session.add(user)
session.commit()

# fetch/update
user2 = session.query(User).get(43)
user2.name='Someone else'
session.commit()

# delete 
session.delete(user2)
session.commit()