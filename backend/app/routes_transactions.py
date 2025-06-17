from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, database
from app.auth import get_current_user

router = APIRouter()

# TRANSACTIONS CRUD
@router.post("/transactions/", status_code=201)
def create_transaction(transaction: models.Transaction, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

@router.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: int, db: Session = Depends(database.SessionLocal)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.get("/transactions/")
def list_transactions(db: Session = Depends(database.SessionLocal)):
    return db.query(models.Transaction).all()

@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(transaction)
    db.commit()
    return {"detail": "Transaction deleted"}

# STOCK MANAGEMENT
@router.post("/vehicles/{vehicle_id}/stock")
def update_vehicle_stock(vehicle_id: int, stock: int, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    vehicle.stock = stock
    db.commit()
    db.refresh(vehicle)
    return vehicle

@router.post("/parts/{part_id}/stock")
def update_part_stock(part_id: int, stock: int, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(get_current_user)):
    part = db.query(models.Part).filter(models.Part.id == part_id).first()
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    part.stock = stock
    db.commit()
    db.refresh(part)
    return part
