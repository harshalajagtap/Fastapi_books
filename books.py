from fastapi import FastAPI

app = FastAPI()

BOOKS={
    "book_1": {"title":"Title One","auther": "Author One"},
    "book_2": {"title":"Title Two","auther": "Author Two"},
    "book_3": {"title":"Title Three","auther": "Author  Three"},
    "book_4": {"title":"Title Four","auther": "Author Four"},
    "book_5": {"title":"Title Five","auther": "Author Five"}
}


@app.get("/")
def read_all_books():
    return BOOKS