from sqlalchemy.orm import Session
from app import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.user.User(name=user.name, email=user.email, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.user.User).filter(models.user.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.user.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, updated_user: schemas.user.UserCreate):
    db_user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    if db_user:
        db_user.name = updated_user.name
        db_user.email = updated_user.email
        db_user.phone = updated_user.phone
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user