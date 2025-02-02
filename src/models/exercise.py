from pydantic import BaseModel


class Exercise(BaseModel):
    id: int
    name: str
    description: str
    instructions: str
    target_muscle: list[str]
    difficulty: str
    category: str
