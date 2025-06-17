from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app import models, database
from app.routes_auth import router as auth_router
from app.routes_crud import router as crud_router
from app.routes_transactions import router as transactions_router
from app.routes_admin import router as admin_router

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(auth_router)
app.include_router(crud_router)
app.include_router(transactions_router)
app.include_router(admin_router)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Vehicles and Parts Management API"}

# Example: List all vehicles
@app.get("/vehicles/")
def list_vehicles(db: Session = Depends(get_db)):
    return db.query(models.Vehicle).all()

# Example: List all parts
@app.get("/parts/")
def list_parts(db: Session = Depends(get_db)):
    return db.query(models.Part).all()

# Example: List all users
@app.get("/users/")
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
