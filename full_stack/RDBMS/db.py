from dotenv import dotenv_values
from sqlalchemy import create_engine

config = dotenv_values(".env")

HOST= config.get("HOST")
DB= config.get("DB")
USER=config.get("USER")
PASSWORD=config.get("PASSWORD")
PORT=config.get("PORT")

def db_engine():
    engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(USER,PASSWORD,HOST,PORT,DB), echo=True,hide_parameters=True)
    return engine