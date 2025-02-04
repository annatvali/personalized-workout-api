from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.routes import auth, exercise, tracking, workout_plan, workout_session
from src.services.database import Base, SessionLocal, engine
from src.services.seed_database import seed_exercises


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    seed_exercises(db)
    db.close()
    yield


app = FastAPI(lifespan=lifespan)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(auth.router)
app.include_router(exercise.router)
app.include_router(workout_plan.router)
app.include_router(tracking.router)
app.include_router(workout_session.router)
