from app.database import Base, engine

from models import *

Base.metadata.create_all(bind=engine)

print("Tables created successfully")
