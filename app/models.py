"""Data models used by the in-memory task store."""

from dataclasses import dataclass


@dataclass
class Task:
    """A task stored by the API."""

    id: int
    title: str
    description: str | None = None
    completed: bool = False
