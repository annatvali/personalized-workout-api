from typing import List

from fastapi import APIRouter, HTTPException

from src.models.tracking import FitnessGoal, WeightEntry
from src.services.tracking_db import (
    add_fitness_goal,
    add_weight_entry,
    delete_fitness_goal,
    get_fitness_goals,
    get_weight_entries,
    update_fitness_goal,
)

router = APIRouter()


@router.get("/weight_entries/{user_id}", response_model=List[WeightEntry])
async def read_weight_entries(user_id: int):
    return get_weight_entries(user_id)


@router.post("/weight_entries", response_model=WeightEntry)
async def create_weight_entry(entry: WeightEntry):
    add_weight_entry(entry)
    return entry


@router.get("/fitness_goals/{user_id}", response_model=List[FitnessGoal])
async def read_fitness_goals(user_id: int):
    return get_fitness_goals(user_id)


@router.post("/fitness_goals", response_model=FitnessGoal)
async def create_fitness_goal(goal: FitnessGoal):
    add_fitness_goal(goal)
    return goal


@router.put("/fitness_goals/{goal_id}", response_model=FitnessGoal)
async def update_fitness_goal_endpoint(goal_id: int, updated_goal: FitnessGoal):
    goal = update_fitness_goal(goal_id, updated_goal)
    if goal is None:
        raise HTTPException(status_code=404, detail="Fitness goal not found")
    return goal


@router.delete("/fitness_goals/{goal_id}", response_model=FitnessGoal)
async def delete_fitness_goal_endpoint(goal_id: int):
    goal = delete_fitness_goal(goal_id)
    if goal is None:
        raise HTTPException(status_code=404, detail="Fitness goal not found")
    return goal
