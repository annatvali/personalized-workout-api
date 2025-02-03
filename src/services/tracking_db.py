from typing import List

from src.models.tracking import FitnessGoal, WeightEntry

weight_entries_db: List[WeightEntry] = []
fitness_goals_db: List[FitnessGoal] = []


def get_weight_entries(user_id: int) -> List[WeightEntry]:
    return [entry for entry in weight_entries_db if entry.user_id == user_id]


def add_weight_entry(entry: WeightEntry) -> None:
    weight_entries_db.append(entry)


def get_fitness_goals(user_id: int) -> List[FitnessGoal]:
    return [goal for goal in fitness_goals_db if goal.user_id == user_id]


def add_fitness_goal(goal: FitnessGoal) -> None:
    fitness_goals_db.append(goal)


def update_fitness_goal(goal_id: int, updated_goal: FitnessGoal) -> FitnessGoal | None:
    for index, goal in enumerate(fitness_goals_db):
        if goal.id == goal_id:
            fitness_goals_db[index] = updated_goal
            return updated_goal
    return None


def delete_fitness_goal(goal_id: int) -> FitnessGoal | None:
    for index, goal in enumerate(fitness_goals_db):
        if goal.id == goal_id:
            return fitness_goals_db.pop(index)
    return None
