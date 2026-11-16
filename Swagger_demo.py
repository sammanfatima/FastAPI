from fastapi import FastAPI
app = FastAPI()

# Define a route
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Swagger Demo!"}

@app.post("/") # post is used to send data to server
async def post_root():
    return{"message": "This is a POST request"}    

@ app.put("/{item_id}")
async def  put_root(item_id: int):
    return {"message": f"Item ID is {item_id}"}
