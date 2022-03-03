from fastapi import APIRouter
from config.db import conn
from models.index import todos
from schemas.index import Todo

todo = APIRouter()

@todo.get("/showTodo")
async def getTodo():
    return conn.execute(todos.select()).fetchall()

@todo.get("/detailTodo/{id}")
async def detailTodo(id:int):
    return conn.execute(todos.select().where(todos.c.id == id)).fetchall()

@todo.post("/createTodo")
async def createTodo(todo: Todo): 
    conn.execute(todos.insert().values(
        name=todo.name,
        isDone=todo.isDone,
        Created_at = todo.Created_at
    ))
    return conn.execute(todos.select()).fetchall()


@todo.put("/updateTodo/{id}")
async def updateTodo(id:int, todo:Todo):
    conn.execute(todos.update().values(
        name=todo.name,
        isDone = todo.isDone,
        Created_at = todo.Created_at
    ).where(todos.c.id == id))
    return conn.execute(todos.select()).fetchall()

@todo.delete("/removeTodo/{id}")
async def deleteTodo(id:int):
    conn.execute(todos.delete().where(todos.c.id==id))
    return conn.execute(todos.select()).fetchall()