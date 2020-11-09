from fastapi import FastAPI, Depends, HTTPException
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import crud
import model
import schemas
from typing import List


# Creates database tables
model.Base.metadata.create_all(bind=engine)


# Creates an instance of the FastAPI Class
app = FastAPI()


# Creates the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Test Route
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/users/', response_model=List[schemas.UserGet])
def read_users():
    pass


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

