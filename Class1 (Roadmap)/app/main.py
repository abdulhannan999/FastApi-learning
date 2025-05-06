from typing import Union

from fastapi import FastAPI

#Fastapi is a class module we initialize it and we use
#its methods to make our App . We use OOP paradigm in our 
#FastApi 



#Here we are making an object our the class
# it will allow us to use the methods using . 
app = FastAPI()


# we use decoraters to use these methods 
#  decoraters mostly start with @

@app.get("/")
async def read_root():
    return {"Hello": "World"}





@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}