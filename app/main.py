from fastapi import FastAPI
from app.routes import user_routes, task_routes

app = FastAPI()

# Include the routers from the user and task routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])
 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
