from fastapi import FastAPI
from routes.index import api_router
import uvicorn

app = FastAPI(title = "Tech Talks API")

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='127.0.0.1')