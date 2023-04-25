from fastapi import FastAPI

from app.core.config import init_db, settings


app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_event():
    await init_db()