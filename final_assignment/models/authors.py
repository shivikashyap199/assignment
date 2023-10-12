from db.db_conn import get_db_conn


conn= get_db_conn()
cursor = conn.cursor()

def get_all_authors():
    cursor.execute("SELECT * FROM Authors")
    authors= cursor.fetchall()
    for author in authors:
        print(author)

def add_author(author_name):
    cursor.execute("INSERT INTO Authors (author_name) VALUES (?)", (author_name))
    conn.commit()
    print("inserted the data successfully!! for author:",author_name)

def remove_author(author_id):
    cursor.execute("DELETE FROM Authors WHERE author_id = ?", (author_id))
    conn.commit()
    print("author details deleted successfully for author_id: ",author_id)

def get_author_by_id(author_id):
    cursor.execute("SELECT * FROM Authors WHERE author_id= ?",(author_id))
    author= cursor.fetchall()
    print(author[0])

def update_author(author_id,author_name):
    cursor.execute("UPDATE Authors SET author_name=? WHERE author_id = ?", (author_name,author_id))
    conn.commit()
    print("author details updated successfully for author_id: ",author_id)
        

