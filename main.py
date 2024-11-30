from database import Base, engine
from backend import app

Base.metadata.create_all(engine)
app.run(host="0.0.0.0")