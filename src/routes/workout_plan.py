from typing import List

from fastapi import APIRouter, HTTPException

from src.models.workout_plan import WorkoutPlan
from src.services.workout_plan_db import (
    add_workout_plan,
    delete_workout_plan,
    get_workout_plan_by_id,
    get_workout_plans,
    update_workout_plan,
)

router = APIRouter()


@router.get("/workout_plans", response_model=List[WorkoutPlan])
async def read_workout_plans():
    return get_workout_plans()


@router.post("/workout_plans", response_model=WorkoutPlan)
async def create_workout_plan(workout_plan: WorkoutPlan):
    add_workout_plan(workout_plan)
    return workout_plan


@router.get("/workout_plans/{plan_id}", response_model=WorkoutPlan)
async def read_workout_plan(plan_id: int):
    plan = get_workout_plan_by_id(plan_id)
    if plan is None:
        raise HTTPException(status_code=404, detail="Workout plan not found")
    return plan


@router.put("/workout_plans/{plan_id}", response_model=WorkoutPlan)
async def update_workout_plan_endpoint(plan_id: int, updated_plan: WorkoutPlan):
    plan = update_workout_plan(plan_id, updated_plan)
    if plan is None:
        raise HTTPException(status_code=404, detail="Workout plan not found")
    return plan


@router.delete("/workout_plans/{plan_id}", response_model=WorkoutPlan)
async def delete_workout_plan_endpoint(plan_id: int):
    plan = delete_workout_plan(plan_id)
    if plan is None:
        raise HTTPException(status_code=404, detail="Workout plan not found")
    return plan
