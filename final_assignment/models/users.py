from db.db_conn import get_db_conn
conn= get_db_conn()
cursor = conn.cursor()

def add_user(username, password):
    cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    print('Inserted the data successfully')

def get_user_reviews(user_id):
    cursor.execute("SELECT * FROM Reviews WHERE user_id = ?", (user_id,))
    result= cursor.fetchall()
    for i in result:
        print(i)
