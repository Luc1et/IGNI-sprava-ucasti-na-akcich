import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

# Načti .env soubor
load_dotenv()

Base = declarative_base()

# Přepni prostředí
ENV = os.getenv("IGNI_ENV", "local")

if ENV == "local":
    DATABASE_URL = os.getenv("DATABASE_URL")  # z .env.local
elif ENV == "prod":
    DATABASE_URL = os.getenv("DATABASE_URL")  # z Railway
else:
    raise ValueError("Neznámé prostředí, zkontroluj IGNI_ENV!")

if not DATABASE_URL:
    raise ValueError("Chybí DATABASE_URL v .env souboru!")

# Async engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Async session factory
AsyncSessionLocal = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

# Dependency pro FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
