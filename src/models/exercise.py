from pydantic import BaseModel


class Exercise(BaseModel):
    id: int
    name: str
    description: str
    instructions: str
    target_muscles: list[str]
    difficulty: str
    category: str
