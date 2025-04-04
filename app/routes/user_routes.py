from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.model_db import User, SessionDep

# Por que preciso instaciar com router e nao com app fastapi?
# Porque o router é um objeto que representa um grupo de rotas, enquanto o app FastAPI é a aplicação principal.

router = APIRouter

@router.post("/")
def create_user(user: User, session: Session):
    session.add(user) # Add user to the database session
    session.commit() # Commit the transaction to the database
    session.refresh(user) # Refresh the user instance to get the updated data from the database
    return user # Return the created user

# Endpoint to get all users
@router.get("/")
def read_users(session: SessionDep):
    users = session.exec(select(User)).all() # Execute a query to get all users from the database
    return users


# How I ll acess the two functions above, if them are the same path 'root'?
# The two functions are differentiated by their HTTP methods: POST and GET.
# The create_user function is called when a POST request is made to the /users/ endpoint