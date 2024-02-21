# fastAPI

## 1. Environment Setup

- Step 1: Create Python Virtual Environment, name `env` (on MacOS)

```Python
python3 -m venv env
```

- Step 2: Activate/Deactivate Virtual Environment on the Terminal

```Python
source env/bin/activate

#to deactivate
deactivate
```

- Step 3: Once the Virtual Enviroment is activated, install packages & dependency

| Package                    | Command                                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------------------- |
| Fast API (Not recommended) | `pip install fastapi[all]` <br>**all**: to include installing all dependencies along with FastAPI package |
| Fast API (Production)      | `pip install fastapi uvicorn[standard]` <br>`uvicorn` to work as the serve                                |
| List installed packages    | `pip freeze`                                                                                              |

- Step 4: Start Fast API server `uvicorn app.main:app --reload`
  - API documentation: http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc

# 2. Tech Stacks

- `Redis` database is used as a broker
- `Celery` is used to create workers that perform the extraction.

# 3. HTTP Code

### Successful responses

- `200` HTTP 200 OK success status response code indicates that the request has succeeded
- `202` HTTP Status 202 indicates that the request has been accepted for processing, but the processing has not been completed.
