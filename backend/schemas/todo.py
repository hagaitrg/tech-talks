from pydantic import BaseModel 
from datetime import datetime

class Todo(BaseModel):
    id:int 
    name:str 
    isDone: bool
    Created_at: datetime.datetime