import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Načti .env soubor (pokud existuje)
load_dotenv()

# Base class pro ORM modely
Base = declarative_base()

# Zjisti prostředí
ENV = os.getenv("IGNI_ENV", "local")  # default: local

if ENV == "pythonanywhere":
    # Připojení na MySQL z proměnných prostředí
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")

    if not all([DB_USER, DB_PASS, DB_NAME, DB_HOST]):
        raise ValueError("Chybí databázové proměnné v .env souboru pro PythonAnywhere!")

    SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
else:
    # Lokální SQLite
    SQLALCHEMY_DATABASE_URL = "sqlite:///./igni_local.db"

# Vytvoření engine a session
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
