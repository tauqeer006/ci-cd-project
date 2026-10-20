"""Task management API routes."""

from fastapi import APIRouter, HTTPException, Response, status

from app import database
from app.models import Task
from app.schemas import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> Task:
    """Create and return a task."""
    return database.create_task(task_data)


@router.get("", response_model=list[TaskResponse])
def list_tasks() -> list[Task]:
    """Return all tasks."""
    return database.list_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int) -> Task:
    """Return one task by its identifier."""
    task = database.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate) -> Task:
    """Replace a task's fields."""
    task = database.update_task(task_id, task_data)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    """Delete a task."""
    if not database.delete_task(task_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
