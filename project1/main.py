from fastapi import FastAPI, Body

app = FastAPI()

books = [
    {'title':'FastAPI essentials', 'author':'najmul', 'published':2025},
    {'title':'FastAPI advanced', 'author':'najmul', 'published':2027},
]

@app.get("/")
async def root():
    return {"message": "Welcome to Project - 1"}

@app.get("/get_books")
async def get_books():
    return {"data": books}

@app.get("/get_book/{book_id}")
async def get_book(book_id: int):
    return {"data": books[book_id]}

@app.post('/create_book')
async def create_book(new_book=Body()):
    books.append(new_book)