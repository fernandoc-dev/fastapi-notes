from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(title='The title',
              description='The description',
              version=1)

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user