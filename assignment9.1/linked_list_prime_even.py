def isPrime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
     
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
 
        return True



class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def swapNodes(self, x, y):
        if x == y:
            return
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
        if currX == None or currY == None:
            return
        if prevX != None:
            prevX.next = currY
        else: 
            self.head = currY
        if prevY != None:
            prevY.next = currX
        else:  
            self.head = currX
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def bubbleSort(self):
        count = 0
        start = self.head
        while start != None:
            count += 1
            start = start.next
        for i in range(0, count):
            start = self.head
            while start != None:
                ptr = start.next
                if ptr != None:
                    if start.data > ptr.data:
                        self.swapNodes(start.data, ptr.data)
                start = start.next

    def find_prime(self):
        list1=[]
        temp=self.head
        while temp!=None:
            if isPrime(temp.data):
                list1.append(temp.data)
            temp=temp.next
        if len(list1) ==0:
            print("No prime numbers")
        else:
            for i in list1:
                print(i,end=" ")
            print()
    
    def find_even(self):
        list1=[]
        temp=self.head
        while temp!=None:
            if (temp.data)%2==0:
                list1.append(temp.data)
            temp=temp.next
        if len(list1) ==0:
            print("No even numbers")
        else:
            for i in list1:
                print(i,end=" ")
            print()

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
