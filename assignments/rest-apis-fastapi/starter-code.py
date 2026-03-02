from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Todo API", description="A simple API for managing todos")

# Pydantic models for request/response validation
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# In-memory storage (replace with database for production)
todos_db: dict = {}
next_id: int = 1

# Root endpoint
@app.get("/", tags=["Root"])
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Todo API", "version": "1.0.0"}

# GET all todos
@app.get("/todos", response_model=List[Todo], tags=["Todos"])
def get_todos(skip: int = 0, limit: int = 10):
    """Retrieve all todos with optional pagination"""
    todos_list = list(todos_db.values())
    return todos_list[skip : skip + limit]

# GET a specific todo
@app.get("/todos/{todo_id}", response_model=Todo, tags=["Todos"])
def get_todo(todo_id: int):
    """Retrieve a specific todo by ID"""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos_db[todo_id]

# POST create a new todo
@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED, tags=["Todos"])
def create_todo(todo: TodoCreate):
    """Create a new todo"""
    global next_id
    new_todo = Todo(
        id=next_id,
        **todo.dict(),
        created_at=datetime.now()
    )
    todos_db[next_id] = new_todo
    next_id += 1
    return new_todo

# PUT update a todo
@app.put("/todos/{todo_id}", response_model=Todo, tags=["Todos"])
def update_todo(todo_id: int, todo: TodoCreate):
    """Update an existing todo"""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    updated_todo = Todo(
        id=todo_id,
        **todo.dict(),
        created_at=todos_db[todo_id].created_at
    )
    todos_db[todo_id] = updated_todo
    return updated_todo

# DELETE a todo
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Todos"])
def delete_todo(todo_id: int):
    """Delete a todo"""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos_db[todo_id]
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
