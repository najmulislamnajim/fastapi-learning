from fastapi import FastAPI

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
        
BOOKS = [
    Book(1,'FastAPI Beginner', 'Najmul Islam', 'Beginner Friendly',5),
    Book(2,'FastAPI Advanced', 'Najmul Islam', 'A very nice book',5),
]

@app.get('/books/')
async def read_all_books():
    return BOOKS