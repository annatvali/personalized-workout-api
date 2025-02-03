from datetime import date
from typing import Optional

from pydantic import BaseModel


class WeightEntry(BaseModel):
    id: Optional[int]
    user_id: int
    date: date
    weight: float  # in kilograms


class FitnessGoal(BaseModel):
    id: Optional[int]
    user_id: int
    goal_type: str
    target_value: float
    current_value: float
    description: Optional[str] = None
    achieved: bool = False
