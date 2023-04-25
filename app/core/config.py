from tortoise import Tortoise

TORTOISE_ORM = {
    "connections":{
        "default": "postgres://postgres:admin@localhost:5432/mvmp",
    },
    "apps": {
        "models": {
            "models": ["aerich.models"],
            "default_connection": "default",
        }
    },
}

async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

class Settings:
    def __init__(self):
        self.PROJECT_NAME = "Multi-vendor Market Place"
        self.DEBUG = True
        self.DATABASE_URL = "default"

settings = Settings()
