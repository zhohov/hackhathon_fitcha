from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


async def get_hashed_password(password: str) -> pwd_context.hash:
    return pwd_context.hash(password)


async def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def auth_user(username: str, password: str):
    return ...
