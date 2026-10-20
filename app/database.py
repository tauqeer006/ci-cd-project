"""Simple in-memory storage for tasks."""

from app.models import Task
from app.schemas import TaskCreate, TaskUpdate

_tasks: dict[int, Task] = {}
_next_task_id = 1


def reset_store() -> None:
    """Clear all tasks and reset the identifier sequence."""
    global _next_task_id
    _tasks.clear()
    _next_task_id = 1


def create_task(task_data: TaskCreate) -> Task:
    """Add a task to the store."""
    global _next_task_id
    task = Task(id=_next_task_id, **task_data.model_dump())
    _tasks[task.id] = task
    _next_task_id += 1
    return task


def list_tasks() -> list[Task]:
    """Return tasks in creation order."""
    return list(_tasks.values())


def get_task(task_id: int) -> Task | None:
    """Find a task by its identifier."""
    return _tasks.get(task_id)


def update_task(task_id: int, task_data: TaskUpdate) -> Task | None:
    """Replace an existing task's fields."""
    existing_task = _tasks.get(task_id)
    if existing_task is None:
        return None

    updated_task = Task(id=task_id, **task_data.model_dump())
    _tasks[task_id] = updated_task
    return updated_task


def delete_task(task_id: int) -> bool:
    """Remove a task and report whether it existed."""
    return _tasks.pop(task_id, None) is not None
