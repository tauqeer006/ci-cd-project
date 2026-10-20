# FastAPI Task Manager

## Set up a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run locally

```powershell
uvicorn app.main:app --reload --port 8080
```

## Run tests

```powershell
pytest -v
```

## Run with Docker Compose

Start the API:

```powershell
docker compose up --build
```

Run the tests in the test profile:

```powershell
docker compose --profile test run test
```

## API documentation

With the API running, open [http://localhost:8080/docs](http://localhost:8080/docs).
