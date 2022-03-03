from fastapi import FastAPI
from routes.index import todo
import uvicorn

app = FastAPI()

app.include_router(todo)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='127.0.0.1')