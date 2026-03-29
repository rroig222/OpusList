from passlib.context import CryptContext

context = CryptContext(
                schemes=["bcrypt"],
                deprecated="auto"
                )

def hash_password(password: str) -> str:

    password = password[:72]
    return context.hash(password)

def verify_password(password: str, password_hash: str) -> bool:

    password = password[:72]
    return context.verify(password, password_hash)