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
    while True:
        try:
            linked_list = LinkedList()
            option = int(input("Please choose what you want do do: 1 for input manually, 2 for generate list, "
                               "0 for exit "))
            if option == 1:
                size = input_size()
                if not check_size(size):
                    print('Size should be 2n')
                    continue
                list_ = linked_list.input_elements(fill_list(size))
                result = list_.swap_halves()
                print(result)
            elif option == 2:
                size = input_size()
                if not check_size(size):
                    print('Size should be 2n')
                    continue
                start = int(input('Enter from which value should we start '))
                end = int(input('Enter a value to which we should generate '))
                list_ = linked_list.generate_list(size, start, end)
                print(list_)
                result = list_.swap_halves()
                print(result)
            elif option == 0:
                print('End of program')
                break
            else:
                print('Unknown option was entered. Try again')
                continue
        except ValueError:
            print('You should have entered an int value. Try again')

menu()