from linked_list import *
from iterator import Iterator
from generator import generate_list


def input_size():
    size = int(input("Enter a size of a list (should be 2n) "))
    return size


def check_size(size):
    return size if size % 2 == 0 else False


def fill_list(size):
    result = []
    for i in range(size):
        element = int(input('Enter an element '))
        result.append(element)
    return result


def input_data():
    option = int(input('Enter 1 for generating a list using an Iterator or 2 using a Generator '))
    length = int(input('Enter a size of a list '))
    start = int(input('Enter a start point '))
    end = int(input('Enter an end point '))
    return option, length, start, end


def menu():
    while True:
        linked_list = LinkedList()
        try:
            option = int(input('Enter 1 if you would like to input values for a list manually or enter 2 for '
                               'generating '))
            if option < 0 or option > 2:
                print('Unknown option was entered. Try again')
                continue
            elif option == 0:
                print('End of a program.')
                break
            elif option == 1:
                linked_list = linked_list.input_elements(fill_list(check_size(input_size())))
                result = linked_list.swap_halves()
                print(result)
                continue
            elif option == 2:
                choice, length, start, end = input_data()
                generator = Iterator(length, start, end) if choice == 1 else generate_list(length, start, end)
                print(linked_list.input_elements(generator))
                result = linked_list.swap_halves()
                print(result)
                continue
            else:
                break
        except ValueError:
            print('An invalid value. Try again')
            continue

menu()