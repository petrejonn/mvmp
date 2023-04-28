from pydantic import BaseSettings
from tortoise import Tortoise

TORTOISE_ORM = {
    "connections":{
        "default": "postgres://postgres:admin@localhost:5432/mvmp",
    },
    "apps": {
        "models": {
            "models": ["aerich.models", "app.user.models.user"],
            "default_connection": "default",
        }
    },
}

async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

class Settings(BaseSettings):
        PROJECT_NAME:str = "Multi-vendor Market Place"
        DEBUG:bool = True
        SECRET_KEY = "3ce71fe213869041e29ee02123ff10fd691d449867a3eb2eb58ce6e32d7d8dd5"
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()
