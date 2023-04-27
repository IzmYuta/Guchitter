from sqlalchemy.orm import Session
import random
from . import models, schemas


def get_guchies(db: Session, limit: int = 4):
    count = db.query(models.Guchi).count()
    num_list = random.sample(range(1, count + 1), limit)  # db上の愚痴から4個ランダムに選ぶ
    return db.query(models.Guchi).filter(models.Guchi.id.in_(num_list)).all()


def get_count(db: Session):
    return db.query(models.Guchi).count()


def create_guchi(db: Session, guchi: schemas.GuchiCreate):
    db_guchi = models.Guchi(**guchi.dict())
    db.add(db_guchi)
    db.commit()
    db.refresh(db_guchi)
    return db_guchi
