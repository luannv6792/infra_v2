from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

# -------------------------------------------------
# JWT CONFIG
# -------------------------------------------------
SECRET_KEY = "CHANGE_ME_IN_PROD"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 8

# -------------------------------------------------
# PASSWORD CONTEXT
# -------------------------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    plain_password: password người dùng nhập (vd: 'admin')
    hashed_password: password đã hash trong DB (bcrypt)
    """
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    """
    Dùng khi tạo user mới
    """
    return pwd_context.hash(password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
