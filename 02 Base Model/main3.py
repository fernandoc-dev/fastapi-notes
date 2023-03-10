from fastapi import FastAPI
from models.user import UserIn,UserOut,fake_save_user

app = FastAPI()

@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved