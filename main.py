import fastapi

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