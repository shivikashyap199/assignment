from db.db_conn import get_db_conn


conn= get_db_conn()
cursor = conn.cursor()

def get_all_books():
    cursor.execute("SELECT * FROM Books")
    books= cursor.fetchall()
    for book in books:
        print(book)

def add_books(title,author_id):
    cursor.execute("INSERT INTO Books (title,author_id) VALUES (?,?)", (title,author_id))
    conn.commit()
    print("inserted the data successfully!!")

def add_book_review(book_id, user_id, user_password, rating, title, details):
    cursor.execute("SELECT password FROM Users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    if result and user_password == result[0]:
        cursor.execute("INSERT INTO Reviews (book_id, user_id, rating, title, details) VALUES (?, ?, ?, ?, ?)",
                       (book_id, user_id, rating, title, details))
        conn.commit()
        return "Review added successfully."
    else:
        return "Invalid user password. Review not added."

def remove_book(book_id):
    cursor.execute("DELETE FROM Books WHERE book_id = ?", (book_id,))
    conn.commit()
    print('Removed the data successfully')

def get_book_by_id(book_id):
    cursor.execute("SELECT * FROM Books WHERE book_id = ?", (book_id,))
    books= cursor.fetchone()
    print(books)

def get_books_by_author_id(author_id):
    cursor.execute("SELECT * FROM Books WHERE author_id = ?", (author_id,))
    result=cursor.fetchall()
    for i in result:
        print(i)

def get_book_reviews(book_id):
    cursor.execute("SELECT * FROM Reviews WHERE book_id = ?", (book_id,))
    result= cursor.fetchall()
    for i in result:
        print(i)