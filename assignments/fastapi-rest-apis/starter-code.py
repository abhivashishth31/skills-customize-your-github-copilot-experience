# FastAPI REST API Starter Code
# Build a complete REST API following the assignment requirements

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(
    title="Assignment API",
    description="A REST API built with FastAPI",
    version="1.0.0"
)

# Define your data models using Pydantic
# Example: Replace Item with your own resource model
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for demonstration
# In production, you would use a database
items_db: List[Item] = []


# TODO: Implement your endpoints below

# Example GET endpoint (replace or expand)
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the FastAPI Assignment!"}


# TODO: Add your POST, PUT, DELETE endpoints here
# Remember to:
# - Use appropriate HTTP methods
# - Define request/response models
# - Add docstrings to your endpoints
# - Handle errors with HTTPException
# - Return appropriate status codes


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
