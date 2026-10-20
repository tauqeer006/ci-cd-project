"""Tests for the Task Manager API."""

from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task(client: TestClient) -> None:
    response = client.post("/tasks", json={"title": "Write tests"})

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Write tests",
        "description": None,
        "completed": False,
    }


def test_create_task_requires_title(client: TestClient) -> None:
    response = client.post("/tasks", json={"description": "No title"})

    assert response.status_code == 422


def test_list_tasks_empty(client: TestClient) -> None:
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_with_data(client: TestClient) -> None:
    client.post("/tasks", json={"title": "First"})
    client.post("/tasks", json={"title": "Second", "completed": True})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert [task["title"] for task in response.json()] == ["First", "Second"]


def test_get_task(client: TestClient) -> None:
    created = client.post("/tasks", json={"title": "Find me"}).json()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json()["title"] == "Find me"


def test_get_task_not_found(client: TestClient) -> None:
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_update_task(client: TestClient) -> None:
    created = client.post("/tasks", json={"title": "Before"}).json()

    response = client.put(
        f"/tasks/{created['id']}",
        json={"title": "After", "description": "Updated", "completed": True},
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": created["id"],
        "title": "After",
        "description": "Updated",
        "completed": True,
    }


def test_update_task_not_found(client: TestClient) -> None:
    response = client.put("/tasks/999", json={"title": "Missing"})

    assert response.status_code == 404


def test_delete_task(client: TestClient) -> None:
    created = client.post("/tasks", json={"title": "Remove me"}).json()

    response = client.delete(f"/tasks/{created['id']}")

    assert response.status_code == 204
    assert client.get(f"/tasks/{created['id']}").status_code == 404


def test_delete_task_not_found(client: TestClient) -> None:
    response = client.delete("/tasks/999")

    assert response.status_code == 404
