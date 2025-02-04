from typing import Type

from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: Type = declarative_base()


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    instructions = Column(String)
    target_muscles = Column(String)
    difficulty = Column(String)
    category = Column(String)


class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    name = Column(String)
    frequency = Column(String)
    goals = Column(String)
    daily_session_duration = Column(Integer)

    exercises = relationship("PlannedExercise", back_populates="workout_plan")


class PlannedExercise(Base):
    __tablename__ = "planned_exercises"

    id = Column(Integer, primary_key=True, index=True)
    workout_plan_id = Column(Integer, ForeignKey("workout_plans.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    repetitions = Column(Integer)
    sets = Column(Integer)
    duration = Column(Integer)
    distance = Column(Float)

    workout_plan = relationship("WorkoutPlan", back_populates="exercises")
    exercise = relationship("Exercise")


class WeightEntry(Base):
    __tablename__ = "weight_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    date = Column(Date)
    weight = Column(Float)


class FitnessGoal(Base):
    __tablename__ = "fitness_goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    goal_type = Column(String)
    target_value = Column(Float)
    current_value = Column(Float)
    description = Column(String)
    achieved = Column(Integer)


class WorkoutSession(Base):
    __tablename__ = "workout_sessions"

    id = Column(Integer, primary_key=True, index=True)
    workout_plan_id = Column(Integer, ForeignKey("workout_plans.id"))
    user_id = Column(Integer, index=True)
    current_exercise_index = Column(Integer)
    completed_exercises = Column(String)
    adjustments = Column(String)

    workout_plan = relationship("WorkoutPlan")
