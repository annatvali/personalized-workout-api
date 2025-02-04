from typing import List

from src.models.workout_plan import WorkoutPlan

workout_plans_db: List[WorkoutPlan] = []


def get_workout_plans() -> List[WorkoutPlan]:
    return workout_plans_db


def add_workout_plan(workout_plan: WorkoutPlan) -> None:
    workout_plans_db.append(workout_plan)


def get_workout_plan_by_id(plan_id: int) -> WorkoutPlan | None:
    for plan in workout_plans_db:
        if plan.id == plan_id:
            return plan
    return None


def update_workout_plan(plan_id: int, updated_plan: WorkoutPlan) -> WorkoutPlan | None:
    for index, plan in enumerate(workout_plans_db):
        if plan.id == plan_id:
            workout_plans_db[index] = updated_plan
            return updated_plan
    return None


def delete_workout_plan(plan_id: int) -> WorkoutPlan | None:
    for index, plan in enumerate(workout_plans_db):
        if plan.id == plan_id:
            return workout_plans_db.pop(index)
    return None
