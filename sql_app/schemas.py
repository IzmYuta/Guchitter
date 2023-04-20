from pydantic import BaseModel


# スキーマファイルはバリデーションのために使われる
class GuchiBase(BaseModel):
    body: str


class GuchiCreate(GuchiBase):
    pass


class Guchi(GuchiBase):
    id: int

    class Config:
        orm_mode = True
