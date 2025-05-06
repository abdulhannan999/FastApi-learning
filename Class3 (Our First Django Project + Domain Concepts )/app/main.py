from typing import Union

from fastapi import FastAPI

# FastAPI is a class module that we initialize. We then use
# its methods to build our application. This demonstrates the
# use of the Object-Oriented Programming (OOP) paradigm in FastAPI.

# Here, we are creating an instance (object) of the FastAPI class.
# This object ('app') will allow us to access the class methods using
# dot notation (e.g., app.get()).
app = FastAPI()

# We use decorators (starting with '@') to associate functions with
# specific HTTP methods and URL paths.

@app.get("/")
async def Home():
    """
    This asynchronous function handles GET requests to the root path ("/").
    It returns a simple JSON response.
    """
    return {"Hello": "World"}


# It seems there's an issue with the 'user' dictionary definition.
# In its current form, later key-value pairs will overwrite earlier ones
# because dictionary keys must be unique. Let's redefine it as a dictionary
# where keys are user IDs and values are user names.

users = {
    "1": "Abdul Hannan",
    "2": "Abdul Rehman",
    "3": "Abdul Malik"
}

@app.get("/users")
async def User():
    
    return {
        "Status": True,
        "Message": "Hello From Users",
        "Data": users
    }

@app.get("/users/{userId}")
async def SingleUser(userId: str):
  
    
    if userId not in users:
        return {"message": "Invalid Request"}
    else:
        return {"user": users[userId]}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}