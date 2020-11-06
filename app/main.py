from fastapi import FastAPI
import schemas

from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/users/', response_model=List[schemas.UserGet])
def read_users():
    pass

@app.post('/users/', response_model=schemas.UserGet)
def create_user(user: schemas.UserCreate):
    user_response = user.dict()
    user_response['user_id'] = 1
    return user_response

