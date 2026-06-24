from fastapi import FastAPI

from app.routes.auth import router as auth_router

app = FastAPI(
    title="Maddy API",
    version="1.0.0"
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Maddy API"
    }