from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymsql://root@localhost:3306/tech_talks")
meta = MetaData()
conn = engine.connect()
