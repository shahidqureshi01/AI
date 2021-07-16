from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_bas
from db import db_engine
import bcrypt

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	last_name = Column(String)
	email = Column(String)
	password_hash = Column(String(256), nullable=False)
	def toJSON(self):
		return {
				'id' : self.id,
				'name': self.name,
				'last_name': self.last_name,
				'email': self.email
		}

	def hash_password(self):
		self.password_hash = bcrypt.hashpw(self.password_hash.encode("utf8"), salt=bcrypt.gensalt()).decode("utf8")
		return self.password_hash

	def check_password(self, password):
		return bcrypt.checkpw(password.encode("utf8"), hashed_password=self.password_hash.encode("utf8"))

#Base.metadata.create_all(engine)