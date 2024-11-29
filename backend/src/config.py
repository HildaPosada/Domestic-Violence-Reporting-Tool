import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__name__), '.env')

load_dotenv(dotenv_path)

db_url = os.environ.get("DATABASE_URL")

if not db_url:
    raise ValueError("DATABASE_URL is not found")
