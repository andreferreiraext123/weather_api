from typing import Annotated
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_name: str = Field(index=True, unique=True)
    area: str = Field(default=None, index=True)


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task_name: str = Field(index=True)
    time_creation: datetime = Field(default_factory=datetime.now)
    user_name: str = Field(default=None, foreign_key="user.user_name")
    user_id: int = Field(default=None, foreign_key="user.id")


sqlite_file_name = "database.db" # DB name
sqlite_url = f"sqlite:///{sqlite_file_name}" #  Where db will be created

# What does the code below do?
# The `connect_args` parameter is used to pass additional arguments to the SQLite database connection.
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

# What does the code below do?
# The `Annotated` type is used to add metadata to the `Session` type.
SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

if __name__ == "__main__":
    create_db_and_tables()