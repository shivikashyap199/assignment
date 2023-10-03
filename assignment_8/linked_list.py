class Node:
    def __init__(self, value, next=None, previous=None):
        self._value = value
        self._next = next
        self._previous = previous

class LinkedList:
    def __init__(self, *args):
        self._first = None
        self._last = None
        self._size = 0
        self.append(*args)

    def append(self, *args):
        for value in args:
            self._append(value)

    def _append(self, value):
        new_node = Node(value, previous=self._last)
        if self._last:
            self._last._next = new_node
        else:
            self._first = new_node
        self._last = new_node
        self._size += 1

    def _len_(self):
        return self._size

    def __locate(self, index):
        if index < 0 or index >= self._len_():
            raise IndexError(f'Invalid Index: {index}')

        n = self._first
        for i in range(index):
            n = n._next

        return n

    def _getitem_(self, index):
        n = self.__locate(index)
        return n._value

    def _setitem_(self, index, value):
        n = self.__locate(index)
        n._value = value

    def insert(self, index, value):
        if index == self._len_():
            self.append(value)
            return
        if index < 0 or index > self._len_():
            raise IndexError(f'Invalid Index: {index}')

        y = self.__locate(index)
        x = y._previous

        new_node = Node(value, previous=x, next=y)

        if x:
            x._next = new_node
        else:
            self._first = new_node

        y._previous = new_node
        self._size += 1

    def remove(self, index):
        n = self.__locate(index)

        x = n._previous
        y = n._next

        if x:
            x._next = y
        else:
            self._first = y

        if y:
            y._previous = x

        self._size -= 1
        return n._value
       
    def remove_all(self):
        while self._first:
            self.remove(0)
        self._last = None    
    
    def _count(self, value):
        count = 0
        n = self._first
        while n:
            if n._value == value:
                count += 1
            n = n._next
        return count
    
    def print_linked_list(self):
        n=self._first
        while n:
            print(n._value)
            n=n._next
        
    def find(self,value):
        n = self._first
        flag=0
        while n:
            if n._value == value:
                print("present in linked list")
                flag=1
                break
            n = n._next
        if flag==0:
            print("Not present in linked list")
            

    def _str_(self):
        if not self._first:
            return "LinkedList(empty)"
        result = "LinkedList(\t"
        n = self._first
        while n:
            result += f'{n._value}\t'
            n = n._next
        result += ")"
        return result

l = LinkedList()
l._append(10)
l._append(20)
l._append(30)
l._append(30)
l._append(30)
l.print_linked_list()
l.remove(3)
l.print_linked_list()
l.remove_all()
l._append(10)
l._append(20)
l._append(30)
l._append(30)
l.print_linked_list()
print(l._len_())
print(l._count(30))
l.find(20)
l.insert(0,40)
l.print_linked_list()