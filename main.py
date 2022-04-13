from logging import root
from fastapi import FastAPI
from uuid import UUID, uuid4
from models import User, Gender, Role
app = FastAPI()

db: list[User] = [
    User(
        id=uuid4(),
        first_name="Johnny",
        last_name="Gaby",
        gender = Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Caleb",
        last_name="Mukwege",
        gender = Gender.female,
        roles=[Role.admin, Role.user]
    ),
]

@app.get("/")
def root():
    return {"Hello": "safi sana", "id": 1}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        else:
            return "User does not exit"