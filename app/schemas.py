"""Pydantic schemas for task requests and responses."""

from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    """Fields required to create a task."""

    title: str
    description: str | None = None
    completed: bool = False


class TaskUpdate(BaseModel):
    """Fields accepted when replacing a task."""

    title: str
    description: str | None = None
    completed: bool = False


class TaskResponse(BaseModel):
    """Task representation returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    completed: bool
