from sqlalchemy.orm import Session

from . import models, schemas


def get_guchies(db: Session, skip: int = 0, limit: int = 4):
    return db.query(models.Guchi).offset(skip).limit(limit).all()


def create_guchi(db: Session, guchi: schemas.GuchiCreate):
    db_guchi = models.Guchi(**guchi.dict())
    db.add(db_guchi)
    db.commit()
    db.refresh(db_guchi)
    return db_guchi
