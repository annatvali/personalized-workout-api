from typing import List

from pydantic import BaseModel


class PlannedExercise(BaseModel):
    exercise_id: int
    repetitions: int
    sets: int
    duration: int  # in seconds
    distance: float  # in meters


class WorkoutPlan(BaseModel):
    id: int
    user_id: int
    name: str
    frequency: str
    goals: str
    exercises: List[PlannedExercise]
    daily_session_duration: int  # in minutes
