from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creates Database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Creates SQLAlchemy Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Creates the class SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Defines the declarative_base function which the database models will inherit from
Base = declarative_base()
