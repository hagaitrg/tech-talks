from pydantic import BaseModel 
from datetime import datetime

class Todo(BaseModel):
    name:str 
    isDone: bool
    Created_at: datetime