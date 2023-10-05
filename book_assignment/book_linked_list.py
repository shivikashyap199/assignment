class Book:
    def __init__(self, id, title, author, price, rating):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

class Node:
    def __init__(self, value, next=None, previous=None):
        self._value = value
        self._next = next
        self._previous = previous

class LinkedList:
    def __init__(self):
        self._first = None

    def append(self, book):
        if self._first is None:
            self._first = Node(book)
        else:
            n = self._first
            while n._next:
                n = n._next
            n._next = Node(book, previous=n)
    def find_by_id(self, id):
        current = self._first
        while current:
            if current._value.id == id:
                return current._value
            current = current._next
        return None

    def find_by_author(self, author):
        list1 = []
        current = self._first
        while current:
            if current._value.author == author:
                list1.append(current._value)
            current = current._next
        return list1

    def find_by_rating_range(self, min_rating, max_rating):
        list1 = []
        current = self._first
        while current:
            if min_rating <= current._value.rating <= max_rating:
                list1.append(current._value)
            current = current._next
        return list1

    def find_by_price_range(self, min_price, max_price):
        list1 = []
        current = self._first
        while current:
            if min_price <= current._value.price <= max_price:
                list1.append(current._value)
            current = current._next
        return list1

l = LinkedList()
l.append(Book(1,"alice in wonderland", "author_abc", 20.99, 4.5))
l.append(Book(2, "monk who sold his ferrari", "author_bcd", 15.99, 3.7))
l.append(Book(3, "hello world", "author_cde", 12.99, 4.2))
l.append(Book(4, "once we meet", "author_fgh", 25.99, 4.8))

response = l.find_by_id(4)
if response:
    print(f"Found book by ID: {response.title}")

response2 = l.find_by_author("author_abc")
print("Books by author_abc:")
for i in response2:
    print(f"{i.title}, by {i.author}")

response3 = l.find_by_rating_range(4.0, 4.5)
print("Books in the rating range 4.0 to 4.5:")
for i in response3:
    print(f"{i.title}, Rating: {i.rating}")

response4 = l.find_by_price_range(15.0, 25.0)
print("Books in the price range $15.0 to $25.0:")
for i in response4:
    print(f"{i.title}, Price: ${i.price}")