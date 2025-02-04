from typing import List

from src.models.workout_plan import WorkoutSession

workout_sessions_db: List[WorkoutSession] = []


def get_workout_sessions(user_id: int) -> List[WorkoutSession]:
    return [session for session in workout_sessions_db if session.user_id == user_id]


def add_workout_session(session: WorkoutSession) -> None:
    workout_sessions_db.append(session)


def get_workout_session_by_id(session_id: int) -> WorkoutSession | None:
    for session in workout_sessions_db:
        if session.id == session_id:
            return session
    return None


def update_workout_session(session_id: int, updated_session: WorkoutSession) -> WorkoutSession | None:
    for index, session in enumerate(workout_sessions_db):
        if session.id == session_id:
            workout_sessions_db[index] = updated_session
            return updated_session
    return None


def delete_workout_session(session_id: int) -> WorkoutSession | None:
    for index, session in enumerate(workout_sessions_db):
        if session.id == session_id:
            return workout_sessions_db.pop(index)
    return None
