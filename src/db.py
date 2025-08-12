from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import src.config as config

DATABASE_URL = (
    f"postgresql+psycopg2://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}"
    f"@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
metadata = MetaData()

prices_table = Table(
    "prices",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("component", String, nullable=False),
    Column("store", String, nullable=False),
    Column("price", Float, nullable=False),
    Column("url", String, nullable=False),
    Column("date", DateTime, default=datetime.utcnow),
)

def init_db():
    metadata.create_all(engine)

def get_session():
    return SessionLocal()
