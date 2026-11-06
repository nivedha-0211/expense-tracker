from fastapi import FastAPI

from app import models
from app.database import Base, engine
from app.routes import users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker")
app.include_router(users.router)


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running"}
