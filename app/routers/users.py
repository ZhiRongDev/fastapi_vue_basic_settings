from fastapi import APIRouter
from app.config import settings

router = APIRouter(tags=["users"])

@router.get("/users")
def read_users():
    print("test1")
    print(settings.ENVIRONMENT)
    print(settings.PROJECT_NAME)
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me")
def read_user_me():
    print("test2")
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}")
def read_user(username: str):
    print("test3")
    return {"username": username}