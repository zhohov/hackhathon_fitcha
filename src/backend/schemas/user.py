from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    username: str
    email: str
    hashed_password: str


class LoginUserSchema(BaseModel):
    username: str
    hashed_password: str
