from fastapi import FastAPI

from src.routes import auth, exercise, workout_plan
from src.services.populate_exercises import populate_exercises

app = FastAPI()

app.include_router(auth.router)
app.include_router(exercise.router)
app.include_router(workout_plan.router)

populate_exercises()
