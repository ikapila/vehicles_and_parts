from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, database
from app.auth import get_current_user

router = APIRouter()

def admin_required(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user

# Promote user to admin
@router.post("/admin/users/{user_id}/promote")
def promote_user(user_id: int, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(admin_required)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_admin = True
    db.commit()
    db.refresh(user)
    return {"detail": f"User {user.username} promoted to admin."}

# Demote user from admin
@router.post("/admin/users/{user_id}/demote")
def demote_user(user_id: int, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(admin_required)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_admin = False
    db.commit()
    db.refresh(user)
    return {"detail": f"User {user.username} demoted from admin."}

# List all users (admin only)
@router.get("/admin/users/")
def admin_list_users(db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(admin_required)):
    return db.query(models.User).all()

# Delete user (admin only)
@router.delete("/admin/users/{user_id}")
def admin_delete_user(user_id: int, db: Session = Depends(database.SessionLocal), current_user: models.User = Depends(admin_required)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": f"User {user.username} deleted."}
