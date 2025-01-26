from pydantic import BaseModel

class Blogcreate(BaseModel):
    id:int
    title:str
    author:str
    class Config:
        from_attributes=True




