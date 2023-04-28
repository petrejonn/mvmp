from datetime import datetime, timedelta
import secrets
from typing import Optional

from jose import jwt

from app.core.config import settings


def create_token():
    return secrets.token_hex(32)
