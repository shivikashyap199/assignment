import pyodbc as db

def get_db_conn():
    driver='{ODBC Driver 18 for SQL Server}'
    server='localhost\SQLExpress'
    database='library_db'
    encrypt='no'
    trusted_connection='yes'

    connection_string=f'''
        DRIVER={driver};
        SERVER={server};
        DATABASE={database};
        TRUSTED_CONNECTION={trusted_connection};
        ENCRYPT={encrypt};
    '''
    print(connection_string)
    connection= db.connect(connection_string)
    if connection:
        print('connection successful')
        return connection
        # print(type(connection))
        # cursor=connection.cursor()
        # result=cursor.execute('SELECT * FROM books' )
        # rows=cursor.fetchall()
        # for i in rows:
        #     print(i)

# if(__name__=='__main__'):
#     main()
