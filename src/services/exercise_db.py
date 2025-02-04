from sqlalchemy.orm import Session

from src.models.exercise import Exercise as ExerciseModel
from src.services.database import Exercise


def get_exercises(db: Session):
    return db.query(Exercise).all()


def add_exercise(db: Session, exercise: ExerciseModel):
    db_exercise = Exercise(
        id=exercise.id,
        name=exercise.name,
        description=exercise.description,
        instructions=exercise.instructions,
        target_muscles=",".join(exercise.target_muscles),
        difficulty=exercise.difficulty,
        category=exercise.category,
    )
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def get_exercise_by_id(db: Session, exercise_id: int):
    return db.query(Exercise).filter(Exercise.id == exercise_id).first()


def update_exercise(db: Session, exercise_id: int, updated_exercise: ExerciseModel):
    db_exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if db_exercise:
        db_exercise.name = updated_exercise.name
        db_exercise.description = updated_exercise.description
        db_exercise.instructions = updated_exercise.instructions
        db_exercise.target_muscles = ",".join(updated_exercise.target_muscles)
        db_exercise.difficulty = updated_exercise.difficulty
        db_exercise.category = updated_exercise.category
        db.commit()
        db.refresh(db_exercise)
    return db_exercise


def delete_exercise(db: Session, exercise_id: int):
    db_exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if db_exercise:
        db.delete(db_exercise)
        db.commit()
    return db_exercise
