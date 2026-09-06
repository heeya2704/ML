import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="Instagram Like Counter API",
    description="FastAPI service for predicting and updating Instagram post likes count",
    version="1.0.0"
)

# Task 4: Custom exception handler to return HTTP 400 Bad Request if fields are missing/invalid
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "status": "error",
            "message": "Bad Request: Missing or invalid required fields. Both 'current_likes' and 'new_likes' must be integers."
        }
    )

# Pydantic Model for Request Body validation
class LikePredictionRequest(BaseModel):
    current_likes: int = Field(..., description="Current count of likes on the post")
    new_likes: int = Field(..., description="Newly added likes to be combined")

@app.get("/")
def read_root():
    """Task 1: Root endpoint returning welcome status message."""
    return {"message": "Instagram Like Counter API running"}

@app.post("/predict-likes")
def predict_likes(payload: LikePredictionRequest):
    """
    Task 2 & 4: POST endpoint calculating updated total likes from JSON payload.
    Returns total_likes along with breakdown.
    """
    total_likes = payload.current_likes + payload.new_likes
    return {
        "status": "success",
        "current_likes": payload.current_likes,
        "new_likes": payload.new_likes,
        "total_likes": total_likes
    }

if __name__ == "__main__":
    # Run FastAPI app locally using Uvicorn on port 8000
    uvicorn.run("insta_like_api:app", host="127.0.0.1", port=8000, reload=True)
