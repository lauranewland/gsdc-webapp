from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creates Database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = 'postgresql://localhost/gsdc_members'

# Creates SQLAlchemy Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creates the class SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Defines the declarative_base function which the database models will inherit from
Base = declarative_base()
