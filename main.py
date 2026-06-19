import fastapi

app = fastapi.FastAPI()
@app.get("/hello")

def message():
    response = {
        "userName" : "Pratik",
        "message" : "Hello, Pratik",
        "directions": "We will add more stuffs in future"
    }
    return response

@app.get("/ping")
def ping():
    return {"status": "alive"}