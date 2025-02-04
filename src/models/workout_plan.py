from typing import List, Optional

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


class WorkoutSession(BaseModel):
    id: int
    workout_plan_id: int
    user_id: int
    current_exercise_index: int
    completed_exercises: List[int]  # exercise IDs
    adjustments: Optional[str] = None
