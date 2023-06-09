from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://guchitter-production.up.railway.app",
    "https://ui-blush.vercel.app"
]
# origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 型定義は変数の後ろに：をつけ、定義する型をその後に書く
@app.get("/api/home")
def read_guchies(db: Session = Depends(get_db)):
    guchies = crud.get_guchies(db)
    return guchies


# response_modelで返却する型を指定できる
@app.post("/api/post", response_model=schemas.Guchi)
# スキーマを定義したものを引数に指定することで、リクエストボディのバリデーションを行う
async def create_guchi(guchi: schemas.GuchiCreate, db: Session = Depends(get_db)):
    return crud.create_guchi(db, guchi=guchi)
