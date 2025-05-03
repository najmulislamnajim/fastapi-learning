from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book:
    id:int
    title:str
    author:str
    description: str
    rating:float 
    
    def __init__(self,id,tittle,author, description, rating):
        self.id=id
        self.title=tittle
        self.author=author
        self.description=description
        self.rating=rating

class BookRequests(BaseModel):
    id:int  
    title:str
    author:str
    description: str
    rating:float 
          
BOOKS = [
    Book(1,'FastAPI Beginner', 'Najmul Islam', 'Beginner Friendly',5),
    Book(2,'FastAPI Advanced', 'Najmul Islam', 'A very nice book',5),
]

@app.get('/books/')
async def read_all_books():
    return BOOKS

@app.post('/create-book/')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)