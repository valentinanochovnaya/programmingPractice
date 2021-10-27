from linked_list import *


def input_size():
    size = int(input("Enter a size of a list (should be 2n) "))
    return size


def check_size(size):
    return True if size % 2 == 0 else False


def fill_list(size):
    result = []
    for i in range(size):
        element = int(input('Enter an element '))
        result.append(element)
    return result


def menu():
    linked_list = LinkedList()
    while True:
        try:
            option = int(input("Please choose what you want do do: 1 for input manually, 2 for generate list, "
                               "0 for exit, 3 for insert, 4 for remove  "))
            if option == 1:
                size = input_size()
                if not check_size(size):
                    print('Size should be 2n')
                    continue
                linked_list = linked_list.input_elements(fill_list(size))
                result = linked_list.swap_halves()
                print(result)
                linked_list = result
            elif option == 2:
                size = input_size()
                if not check_size(size):
                    print('Size should be 2n')
                    continue
                start = int(input('Enter from which value should we start '))
                end = int(input('Enter a value to which we should generate '))
                linked_list = linked_list.generate_list(size, start, end)
                print(linked_list)
                result = linked_list.swap_halves()
                print(result)
                linked_list = result
            elif option == 3:
                input_ = int(input('Enter what should be inserted into a list '))
                position = int(input('Enter a position on which a value should be inserted '))
                if position > len(linked_list):
                    print('There is not such a position')
                    continue
                print(linked_list.insert(input_, position))
            elif option == 4:
                position = int(input('Enter a position on which a value should be removed '))
                if position > len(linked_list):
                    print('There is not such a position')
                    continue
                print(linked_list.remove(position))
            elif option == 0:
                print('End of program')
                break
            else:
                print('Unknown option was entered. Try again')
                continue
        except ValueError:
            print('You should have entered an int value. Try again')

menu()