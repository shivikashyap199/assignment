from db.db_conn import get_db_conn

conn= get_db_conn()
cursor= conn.cursor()

def create_tables():
    cursor.execute('''
        CREATE TABLE Authors (
            author_id INT IDENTITY(1,1) PRIMARY KEY,
            author_name VARCHAR(255)
        )
    ''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE Books (
            book_id INT IDENTITY(1,1) PRIMARY KEY,
            title VARCHAR(255),
            author_id INT,
            FOREIGN KEY (author_id) REFERENCES Authors(author_id)
        )
    ''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE Users (
            user_id INT IDENTITY(1,1) PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255)
        )
    ''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE Reviews (
            review_id INT IDENTITY(1,1) PRIMARY KEY,
            book_id INT,
            user_id INT,
            rating INT,
            title VARCHAR(255),
            details VARCHAR(1000),
            FOREIGN KEY (book_id) REFERENCES Books(book_id),
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    ''')
    conn.commit()