from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List
import crud
import model
import schemas


# Creates database tables
model.Base.metadata.create_all(bind=engine)


# Creates an instance of the FastAPI Class
app = FastAPI()


def get_db():
    """Creates the database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    """Test Route"""
    return {"message": "Hello World"}


# API Get Response_Model will return a list of all users
@app.get('/users/', response_model=List[schemas.UserGet])
def read_all_users(db: Session = Depends(get_db)):
    """Returns a all users"""

    users = crud.get_all_users(db)
    return users


# Response_model is what will be returned from the post
@app.post('/users/', response_model=schemas.UserGet)
def create_user(post_body: schemas.UserCreate, db: Session = Depends(get_db)):
    """Returns a newly created user

    .. note::

        :raise: HTTPException if the users email address already exist in the database
        :returns: Creates a new user in the database
    """
    db_user = crud.get_user_by_email(db, email=post_body.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=post_body)


@app.post('/users/{user_id}/interest/', response_model=schemas.Interest)
def create_interest_for_user(user_id: int, post_body: schemas.CreateInterest, db: Session = Depends(get_db)):
    """Returns a newly created item"""
    return crud.create_user_interest(db=db, interest=post_body, user_id=user_id)
