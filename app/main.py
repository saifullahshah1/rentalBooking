from fastapi import FastAPI
from app.routers import users
from app.database import Base, engine
from app import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Rental Booking API - MVP1")

app.include_router(users.router)