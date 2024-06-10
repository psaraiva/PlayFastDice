import random
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"salutation": "Play Fast Dice"}

@app.get("/api/dice/play")
def play(quantity: int = 1, face: int = 6):
    if quantity < 1 or quantity > 5:
        return {"error": "Quantity must be between 1 and 6"}

    vfaces = [4,6,8,10,12,13,14,15,16,17,18,19,20]
    if (face < 2 or face > 100) or face not in vfaces:
        return {"error": "Face value is not valid"}

    result = [random.randint(1, face) for _ in range(quantity)]
    return {"dice": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)