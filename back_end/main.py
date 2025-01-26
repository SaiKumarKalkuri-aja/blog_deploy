from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from models import *
from database import *
from schemas import *

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

@app.post("/blogs/", response_model=Blogcreate)
def create_blog(blog: Blogcreate, db:Session = Depends(get_db)):
    db_blog = Blog(id=blog.id,title=blog.title, author=blog.author)
    db.add(db_blog)
    db.commit() 
    db.refresh(db_blog)
    return db_blog

@app.get("/blogs/", response_model=List[Blogcreate])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs