import fastapi
from pydantic import BaseModel

class cloneBase(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

app = fastapi.FastAPI()
@app.get("/hello/{userName}")
def message(userName):
    response = {
        "userName" : userName,
        "message" : f"Hello,{userName}",
        "directions": "We will add more stuffs in future"
    }
    return response

@app.get("/ping")
def ping():
    return {"status": "alive"}

@app.post("/echo")
def echo(payload: cloneBase):
    results = {
        "id": payload.id,
        "name":payload.name,
        "email": payload.email,
        "is_active": payload.is_active
    }
    return results