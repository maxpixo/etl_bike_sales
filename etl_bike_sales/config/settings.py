from dotenv import load_dotenv
load_dotenv(override=True) 
import os


load_dotenv()


DB_CONFIG = {
    "host": os.getenv("PG_HOST"),
    "port": os.getenv("PG_PORT"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
    "database": os.getenv("PG_DB")
}

# 🧪 Print to debug
print(f"[DEBUG] DB_CONFIG = {DB_CONFIG}")