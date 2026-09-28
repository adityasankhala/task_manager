from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi_taskmanager.routers import health

app = FastAPI()
app.include_router(health.router)

@app.get('/')
def home():
    return {"message": "welcome task manager app !"}

class LoginData(BaseModel):
    email: str
    password: str

@app.post("/auth/login")
def login(data: LoginData):
    return {"message": f"Successfully received login attempt for {data.email}"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "email": "admin@example.com", "role": "admin"},
        {"id": 2, "email": "intern@example.com", "role": "user"}
    ]
