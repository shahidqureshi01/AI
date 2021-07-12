import os 
from dotenv import dotenv_values, load_dotenv
from sqlalchemy import create_engine
load_dotenv()

HOST= os.getenv("HOST")
DB= os.getenv("DB")
USER=os.getenv("DB")
PASSWORD=os.getenv("PASSWORD")
PORT=os.getenv("PORT")

def db_engine():
    engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(USER,PASSWORD,HOST,PORT,DB), echo=True,hide_parameters=True)
    return engine

print(db_engine())