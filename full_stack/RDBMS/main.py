from python_dotenv import dotenv_values

config = dotenv_values(".env")

HOST= config.get("HOST")
DB= config.get("DB")
USER=config.get("USER")
PASSWORD=config.get("PASSWORD")
PORT=config.get("PORT")