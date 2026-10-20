"""Shared pytest fixtures."""

import pytest
from fastapi.testclient import TestClient

from app.database import reset_store
from app.main import app


@pytest.fixture
def client() -> TestClient:
    """Provide a test client for the API."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_task_store() -> None:
    """Reset task storage before each test."""
    reset_store()
