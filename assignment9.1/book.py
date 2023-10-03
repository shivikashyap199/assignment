class Book:
    def __init__(self, id, title, author, price, rating):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating



def find_book_id(books,book_id):
    for i in books:
        if i.id == book_id:
            return i
    return None

def find_books_by_author(books,author_name):
    list1=[]
    for i in books:
        if i.author == author_name:
            list1.append(i)
    return list1

def find_books_in_rate(books,min_rating, max_rating):
    list1=[]
    for i in books:
        if min_rating <= i.rating <= max_rating:
            list1.append(i)
    return list1

def find_books_in_price(books,min_price, max_price):
    list1=[]
    for i in books:
        if min_price <= i.price <= max_price:
            list1.append(i)
    return list1

    