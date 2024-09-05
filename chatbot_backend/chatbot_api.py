from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def get_response(message:str):
    return {"response": f"hello"}
