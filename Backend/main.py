from fastapi import FastAPI

app = FastAPI(
    title="Maddy API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Maddy API"
    }