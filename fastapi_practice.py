# Practicing FastAPI

from fastapi import FastAPI, Path
from typing import Optional

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

# Combininig Query and Path
@app.get("/combine-user/{user_id}") #path parameter
# def combined_user(*, name: Optional[str] = None, user_id: int):
#     for user_id in users:
#         if users[user_id]['name'] == name:
#             return users[user_id]
        
#         return users[user_id]
#     if user_id not in users:
#         return {"Error": "User not found"}
    
# Gets the user details using user id and optionally name
def combined(user_id: int, name: Optional[str] = None):
    if user_id not in users:
        return {"Error": "User not found"}
    
    user = users[user_id]
    if name != None:
        if user["name"] == name:
            return user
        else:
            return {"Error": "Name does not match User ID"}
    
    return user

