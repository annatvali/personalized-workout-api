from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.exercise import Exercise as ExerciseModel
from src.services.database import SessionLocal
from src.services.exercise_db import add_exercise, delete_exercise, get_exercise_by_id, get_exercises, update_exercise

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/exercises", response_model=List[ExerciseModel])
async def read_exercises(db: Session = Depends(get_db)):
    return get_exercises(db)


@router.post("/exercises", response_model=ExerciseModel)
async def create_exercise(exercise: ExerciseModel, db: Session = Depends(get_db)):
    return add_exercise(db, exercise)


@router.get("/exercises/{exercise_id}", response_model=ExerciseModel)
async def read_exercise(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = get_exercise_by_id(db, exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return db_exercise


@router.put("/exercises/{exercise_id}", response_model=ExerciseModel)
async def update_exercise_endpoint(exercise_id: int, updated_exercise: ExerciseModel, db: Session = Depends(get_db)):
    db_exercise = update_exercise(db, exercise_id, updated_exercise)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return db_exercise


@router.delete("/exercises/{exercise_id}", response_model=ExerciseModel)
async def delete_exercise_endpoint(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = delete_exercise(db, exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return db_exercise
