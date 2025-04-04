from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.model_db import User, Task, SessionDep

router = APIRouter()

# Creat a new task
@router.post("/")
def create_task(task: Task, session: Session):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

# Show all taks
@router.get("/")
def read_taks(session: SessionDep):
    tasks = Session.exec(select(Task)).all() # Execute a query to get alal tasks from the database
    return tasks

# Endpoint to get a task by ID
@router.get("/{task_id}")
def read_task(task_id: int, session: SessionDep):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found") # Execute a query to get a task by ID from the database
    return task


# Endpoint to update a task
@router.put("/{task_id}")
def update_task(task_id: int, updated_task: Task, session: SessionDep):
    task = session.get(Task, task_id)  # Retrieve the task by its ID
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in updated_task.dict(exclude_unset=True).items():
        setattr(task, key, value)  # Update the task fields
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

# Endpoint to delete a task
@router.delete("/{task_id}")
def delete_task(task_id: int, session: SessionDep):
    task = session.get(Task, task_id)  # Retrieve the task by its ID
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)  # Delete the task from the database
    session.commit()
    return {"message": "Task deleted successfully"}