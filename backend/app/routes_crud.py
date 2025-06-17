from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, database
from app.auth import get_current_user

router = APIRouter()

# VEHICLES CRUD
@router.post("/vehicles/", status_code=201)
def create_vehicle(vehicle: models.Vehicle, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

@router.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int, db: Session = Depends(database.SessionLocal)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.put("/vehicles/{vehicle_id}")
def update_vehicle(vehicle_id: int, updated: models.Vehicle, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    for attr, value in updated.__dict__.items():
        if attr != "id" and value is not None:
            setattr(vehicle, attr, value)
    db.commit()
    db.refresh(vehicle)
    return vehicle

@router.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    db.delete(vehicle)
    db.commit()
    return {"detail": "Vehicle deleted"}

# PARTS CRUD
@router.post("/parts/", status_code=201)
def create_part(part: models.Part, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    db.add(part)
    db.commit()
    db.refresh(part)
    return part

@router.get("/parts/{part_id}")
def get_part(part_id: int, db: Session = Depends(database.SessionLocal)):
    part = db.query(models.Part).filter(models.Part.id == part_id).first()
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@router.put("/parts/{part_id}")
def update_part(part_id: int, updated: models.Part, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    part = db.query(models.Part).filter(models.Part.id == part_id).first()
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    for attr, value in updated.__dict__.items():
        if attr != "id" and value is not None:
            setattr(part, attr, value)
    db.commit()
    db.refresh(part)
    return part

@router.delete("/parts/{part_id}")
def delete_part(part_id: int, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    part = db.query(models.Part).filter(models.Part.id == part_id).first()
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    db.delete(part)
    db.commit()
    return {"detail": "Part deleted"}
