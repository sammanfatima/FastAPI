from fastapi import FastAPI
app = FastAPI()

# Define a route
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Swagger Demo!"}

@app.post("/") # post is used to send data to server
async def post_root():
    return{"message": "This is a POST request"}    

# @ app.put("/{item_id}")
# async def  put_root(item_id: int):
#     return {"message": f"Item ID is {item_id}"}


@app.get("/items")  
async def get_item():
    return{"message": "This route will list items"}  

# add path parameters in the route items as item ids
@app.get("/items/{item_id}")  
async def get_item(item_id):
    return{"item_id": item_id}

# same path parameter for user
@app.get("/users")
async def get_users():
    return{"message":" This route will list users"}

@app.get("/users/{user_id}") 
async def get_user(user_id: int): # user id will be unique with numeric value
    return{"user_id": user_id}   