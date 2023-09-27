class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_last(self, value):
        new = Node(value)
        if self.head == None and self.tail==None:
            self.head = new

        elif self.head == self.tail:
            self.head.next = new

        else:
            self.tail.next = new

        self.tail = new
        self.len += 1


    def insert_node(self, data, pos):
        new = Node(data)
        node = self.head if pos==0 else self.get(pos-1)

        if node:
            new.next = node.next
            node.next = new
            self.len += 1
        
    def get_value(self, pos):
        data = self.get(pos)
        if(data):
            return data.data
        
    def get(self, pos):
        temp = self.head
        count = 0
        while temp != None:
            if(count==pos):
                return temp
            count+=1
            temp = temp.next
        return Node(None)

    def set_value(self, data, pos):
        node = self.get(pos)
        if(isinstance(node, Node)):
            node.data = data


    def size(self):
        temp = self.head
        count = 0
        while temp != None:
            temp = temp.next
            count+=1
        return count 

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def info(self):
        print('List elements : ', end='')
        self.print_list()
        print(f'\nSize {self.len}')

    def delete(self, pos):
        temp = self.head
        deleted_node = None
        count = 0
        if(pos == 0):
            deleted_node = self.head
            self.head = self.head.next

        elif pos<self.len:

            while temp != None:
                if count==pos-1:
                    deleted_node = temp.next
                    if temp.next.next != None:
                        temp.next = temp.next.next
                        break
                    
                    else:
                        temp.next = None
                        break

                count+=1
                temp = temp.next

        if(deleted_node != None):
            self.len -= 1

        return deleted_node
        
    
    def clear(self):
        temp = self.head
        while temp != None:
            self.remove(0)
            temp = temp.next
