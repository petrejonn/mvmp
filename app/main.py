from fastapi import FastAPI
from app.authentication.endpoints import auth
from app.core.config import init_db, settings
from app.user.endpoints import user


app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(auth.router)
app.include_router(user.router)

@app.on_event("startup")
async def startup_event():
    await init_db()