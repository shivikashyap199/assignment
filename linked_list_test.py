from linked_list import LinkedList


def main():
    list = LinkedList()


    for x in range(10, 200, 10):
        list.add_last(x)

    list.info()

    print(f'Element present at index {1}: {list.get(1)}')
    print(f'Value of element present at index {1}: {list.get_value(1)}')

    print('Adding elements to list')
    list.insert_node(30, 1)
    list.insert_node(33, 0)
    list.insert_node(4567, 0)
    list.info()
    print()

    print('Removing elements from list')
    list.delete(0)
    list.delete(13)

    list.info()

if(__name__=='__main__'):
    main()