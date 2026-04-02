from fastapi import FastAPI
from database import engine, Base

# Create database tables on startup if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "connected", "database": "Google Cloud MySQL"}