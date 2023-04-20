from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 型定義は変数の後ろに：をつけ、定義する型をその後に書く
@app.get("/", response_model=list[schemas.Guchi])
def read_guchies(db: Session = Depends(get_db)):
    guchies = crud.get_guchies(db)
    return guchies


# response_modelで返却する型を指定できる
@app.post("/post/", response_model=schemas.Guchi)
# スキーマを定義したものを引数に指定することで、リクエストボディのバリデーションを行う
async def create_guchi(guchi: schemas.GuchiCreate, db: Session = Depends(get_db)):
    return crud.create_guchi(db, guchi=guchi)
