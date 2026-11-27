from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

import os


def database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if url:
        return url
    password = os.getenv("POSTGRES_PASSWORD")
    if not password:
        raise RuntimeError("Set DATABASE_URL or POSTGRES_PASSWORD")
    user = os.getenv("POSTGRES_USER", "postgres")
    host = os.getenv("POSTGRES_HOST", "db")
    port = os.getenv("POSTGRES_PORT", "5432")
    name = os.getenv("POSTGRES_DB", "ParsNewsDB")
    return f"postgresql://{user}:{password}@{host}:{port}/{name}"


engine = create_engine(database_url())

Base = declarative_base()

# Определение таблиц
class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    news = relationship("News", uselist=False, back_populates="link")

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    link_id = Column(Integer, ForeignKey('links.id'), unique=True)
    news_id = Column(String, unique=True)
    date = Column(TIMESTAMP)
    time = Column(String)
    title = Column(String)
    text = Column(Text)
    link = relationship("Link", back_populates="news")

# Создание таблиц
Base.metadata.create_all(engine)
