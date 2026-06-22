# app/main.py

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Document Processing System",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {"status": "running"}