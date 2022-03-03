from sqlalchemy.sql.sqltypes import Integer,String, Boolean, DateTime
from sqlalchemy import Table, Column 
from config.db import meta 
from datetime import datetime

todos = Table(
    'todos',meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), unique=True),
    Column('isDone', Boolean, unique=True, default=False),
    Column('Created_at', DateTime, default=datetime.now),
)