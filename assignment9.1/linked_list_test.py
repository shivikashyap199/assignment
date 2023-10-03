from linked_list_prime_even import LinkedList


def main():
    list = LinkedList()


    for x in range(10, 200, 10):
        list.add_last(x)

    list.info()

    print(f'Element present at index {1}: {list.get(1)}')
    print(f'Value of element present at index {1}: {list.get_value(1)}')

    print('Adding elements to list')
    list.insert_node(33, 1)
    list.insert_node(4567, 0)
    print("Prime Numbers in the linkedlist:")
    list.find_prime()
    print("Even numbers in the list:")
    list.find_even()
    print("The Sorted linked list:")
    list.bubbleSort()
    list.print_list()
    list.info()
    print()

    print('Removing elements from list')
    list.delete(0)
    list.delete(13)

    list.info()

if(__name__=='__main__'):
    main()