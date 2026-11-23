from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: str):

    if user_id.isdigit():
        return {
            "user_id": int(user_id),
            "type": "Integer ID"
        }

    else:
        return {
            "user_id": user_id,
            "type": "String ID"
        }