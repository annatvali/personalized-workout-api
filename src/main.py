from fastapi import FastAPI

from src.routes import auth, exercise
from src.services.populate_exercises import populate_exercises

app = FastAPI()

app.include_router(auth.router)
app.include_router(exercise.router)

populate_exercises()
