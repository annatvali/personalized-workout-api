from fastapi import APIRouter, HTTPException

from src.models.exercise import Exercise
from src.services.exercise_db import add_exercise, delete_exercise, get_exercise_by_id, get_exercises, update_exercise

router = APIRouter()


@router.get("/exercises", response_model=list[Exercise])
async def read_exercises():
    return get_exercises()


@router.post("/exercises", response_model=Exercise)
async def create_exercise(exercise: Exercise):
    add_exercise(exercise)
    return exercise


@router.get("/exercises/{exercise_id}", response_model=Exercise)
async def read_exercise(exercise_id: int):
    exercise = get_exercise_by_id(exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise


@router.put("/exercises/{exercise_id}", response_model=Exercise)
async def update_exercise_endpoint(exercise_id: int, updated_exercise: Exercise):
    exercise = update_exercise(exercise_id, updated_exercise)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise


@router.delete("/exercises/{exercise_id}", response_model=Exercise)
async def delete_exercise_endpoint(exercise_id: int):
    exercise = delete_exercise(exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise
