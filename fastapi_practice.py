# Practicing FastAPI

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1 : {
        "name": "Simeon",
        "age": 52,
        "year": "level 9"
    },

    2 : {
        "name": "Adebo",
        "age": 50,
        "year": "level 9"
    }
}

# Get endpoint: gets information
@app.get("/") # This takes it to the home
def index():
    return {"Home": "Welcome to the first trial."}

# Path parameter
@app.get("/get_user/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        return {"Error": "User not found"}
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


# REQUEST BODY AND POST METHOD

class User(BaseModel):
    name: str
    age: int
    year: str

# Post method, creates or adds new information
# The class User makes up the request body
@app.post("/create-user{user_id}")
def create_user(user_id: int, user : User):
    if user_id in users:
        return {"Error": "User exists"}
    # This saves the input from 'user' to the dictionary 'users' using the 'user_id'
    users[user_id] = user
    return users[user_id]


# PUT Method, updates or changes an existing information
class Update(BaseModel):
    #making it optional so it doesn't update fields that weren't provided by the user
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.post("/update-user/{user_id}")
def update_user(user_id: int, user: Update):
    if user_id not in users:
        return {"Error": "Student not found"}
    # This ensures that it only updates the fields provided, and it doesn't overwrite the ones not provided
    if user.name != None:
        users[user_id]["name" ]= user.name
    if user.age != None:
        users[user_id]["age"] = user.age
    if user.year != None:
        users[user_id]["year"] = user.year
    return users[user_id]

