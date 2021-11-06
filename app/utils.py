from passlib.context import CryptContext
# passlib context bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def hash(password: str):
    return pwd_context.hash(password)
