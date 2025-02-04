from typing import List

from fastapi import APIRouter, HTTPException

from src.models.workout_plan import WorkoutSession
from src.services.workout_session_db import (
    add_workout_session,
    delete_workout_session,
    get_workout_session_by_id,
    get_workout_sessions,
    update_workout_session,
)

router = APIRouter()


@router.get("/workout_sessions/{user_id}", response_model=List[WorkoutSession])
async def read_workout_sessions(user_id: int):
    return get_workout_sessions(user_id)


@router.post("/workout_sessions", response_model=WorkoutSession)
async def create_workout_session(session: WorkoutSession):
    add_workout_session(session)
    return session


@router.get("/workout_sessions/session/{session_id}", response_model=WorkoutSession)
async def read_workout_session(session_id: int):
    session = get_workout_session_by_id(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Workout session not found")
    return session


@router.put("/workout_sessions/session/{session_id}", response_model=WorkoutSession)
async def update_workout_session_endpoint(session_id: int, updated_session: WorkoutSession):
    session = update_workout_session(session_id, updated_session)
    if session is None:
        raise HTTPException(status_code=404, detail="Workout session not found")
    return session


@router.delete("/workout_sessions/session/{session_id}", response_model=WorkoutSession)
async def delete_workout_session_endpoint(session_id: int):
    session = delete_workout_session(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Workout session not found")
    return session
