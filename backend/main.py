from fastapi import FastAPI
from routes.generate import router as generate_router

app = FastAPI(title="AI Video SaaS")

app.include_router(generate_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "AI Video SaaS Running"}
