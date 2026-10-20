"""FastAPI application entry point."""

from fastapi import FastAPI

from app.routes.tasks import router as tasks_router

app = FastAPI(title="Task Manager API")
app.include_router(tasks_router)


@app.get("/health")
def health() -> dict[str, str]:
    """Return the application health status."""
    return {"status": "ok"}
