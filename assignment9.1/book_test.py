from book import Book, find_book_id, find_books_by_author, find_books_in_price, find_books_in_rate

def main():
    books = [
        Book(1, "alice in wonderland", "author_abc", 20.99, 4.5),
        Book(2, "monk who sold his ferrari", "author_bcd", 15.99, 3.7),
        Book(3, "hello world", "author_cde", 12.99, 4.2),
        Book(4, "once we meet", "author_fgh", 25.99, 4.8),
    ]
    print("Find a book by Id:")
    response = find_book_id(books,2)
    if response:
        print(f"Book found: {response.title} by {response.author}")
    else:
        print("Book not found")

    print("\n Find all books by an author:")
    response2 = find_books_by_author(books,"Author1")
    if response2:
        for i in response2:
            print(f"{i.title} by {i.author}")
    else:
        print("No books by this author")

    print("\n Find all books in a rating range:")
    response3 = find_books_in_rate(books,4.0, 4.5)
    if response3:
        for i in response3:
            print(f"{i.title} has a rating of {i.rating}")
    else:
        print("No books in this rating range")

    print("\n Find all books in a price range:")
    response4 = find_books_in_price(books,10.0, 20.0)
    if response4:
        for i in response4:
            print(f"{i.title} is priced at ${i.price}")
    else:
        print("No books in this price range")



if(__name__=='__main__'):
    main()