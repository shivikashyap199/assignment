from models.create_models import create_tables
from models.authors import add_author,get_all_authors,remove_author,get_author_by_id,update_author
from models.books import add_books,get_all_books,add_book_review,remove_book,get_book_by_id,get_books_by_author_id,get_book_reviews
from models.users import add_user,get_user_reviews
#create_tables()  #This will be called only once as it is used to create the table


command_mapping = {
    'get_all_authors': get_all_authors,
    'add_author': add_author,
    'remove_author':remove_author,
    'get_author_by_id':get_author_by_id,
    'add_books':add_books,
    'get_all_books':get_all_books,
    'update_author':update_author,
    'add_book_review':add_book_review,
    'remove_book':remove_book,
    'get_book_by_id':get_book_by_id,
    'get_books_by_author_id':get_books_by_author_id,
    'get_book_reviews':get_book_reviews,
    'add_user':add_user,
    'get_user_reviews':get_user_reviews

     

}

exit_commands = {'quit', 'exit', 'bye'}


while True:
    user_input = input("db> ").strip().lower()
    
    if user_input in exit_commands:
        print("Exiting the shell.")
        break

    
    parts = user_input.split(',')
    if parts:
        command, *args = parts
        if command in command_mapping:
            result = command_mapping[command](*args)
            if result is not None:
                print(result)
        else:
            print("Command not recognized.")

