from typing import List

from src.models.exercise import Exercise

exercises_db: List[Exercise] = []


def get_exercises() -> List[Exercise]:
    return exercises_db


def add_exercise(exercise: Exercise) -> None:
    exercises_db.append(exercise)


def get_exercise_by_id(exercise_id: int) -> Exercise | None:
    for exercise in exercises_db:
        if exercise.id == exercise_id:
            return exercise
    return None


def update_exercise(exercise_id: int, updated_exercise: Exercise):
    for index, exercise in enumerate(exercises_db):
        if exercise.id == exercise_id:
            exercises_db[index] = updated_exercise
            return updated_exercise
    return None


def delete_exercise(exercise_id: int) -> Exercise | None:
    for index, exercise in enumerate(exercises_db):
        if exercise.id == exercise_id:
            return exercises_db.pop(index)
    return None
