# Practicing FastAPI

from fastapi import FastAPI, Path, Optional

app = FastAPI()

users = {
    1 : {
        "name": "Simeon",
        "age": 52,
        "level": "level 9"
    }
}

# Get endpoint: gets information
@app.get("/") # This takes it to the home
def index():
    return {"Home": "Welcome to the first trial."}

# Path parameter
@app.get("/get_user/{user_id}")
def get_user(user_id: int):
    return users[user_id]

# Query parameter
@app.get("/get_using_name")
def using_name(name: str):
    for user in users:
        if users[user]["name"] == name:
            return users
    return {"Data": "Not found"}