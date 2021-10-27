from random import *


class Node:
    def __init__(self, value=None, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class LinkedList:
    def __init__(self):
        self.first_node = Node()
        self.size = 0
        self.tail = None

    def __len__(self):
        return self.size

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        string = ' '
        for i in range(self.size):
            string += str(self[i]) + ' '
        return string

    def __iter__(self):
        self.current = self.first_node
        return self

    def __getitem__(self, index):
        current = self.first_node
        i = -1
        while current is not None:
            i += 1
            if i == index:
                return current.value
            current = current.next

    def __setitem__(self, index, value):
        current = self.first_node
        i = -1
        while current.value is not None:
            i += 1
            if i == index:
                current.value = value
                return
            current = current.next

    def check_first_node(self):
        return True if self.first_node.value is None else False

    def add_first_node(self, value):
        element = Node(value)
        self.first_node = element
        return

    def append(self, data):
        if self.first_node is None:
            self.first_node = Node(data)
            self.tail = self.first_node
            self.size += 1
            return

        self.tail.next = Node(data)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.size += 1

    def insert(self, data, index):
        if (index > self.size) | (index < 0):
            return
        if index == self.size:
            self.append(data)
            return
        if index == 0:
            self.first_node.previous = Node(data)
            self.first_node.previous.next = self.first_node
            self.first_node = self.first_node.previous
            self.size += 1
            return
        start = self.first_node
        for _ in range(index):
            start = start.next
        start.previous.next = Node(data)
        start.previous.next.previous = start.previous
        start.previous.next.next = start
        start.previous = start.previous.next
        self.size += 1
        return self

    def remove(self, index):
        if (index >= self.size) | (index < 0):
            return
        if index == 0:
            self.first_node = self.first_node.next
            self.first_node.previous = None
            self.size -= 1
            return
        if index == (self.size - 1):
            self.tail = None
            self.size -= 1
            return self
        start = self.first_node
        for i in range(index):
            start = start.next
        start.previous.next, start.next.previous = start.next, start.previous
        self.size -= 1
        return self

    def insert_at_end(self, value):
        if self.check_first_node():
            self.add_first_node(value)
            self.size += 1
            return
        current = self.first_node
        while current.next is not None:
            current = current.next
        element = Node(value)
        current.next = element
        element.previous = current
        self.size += 1

    def input_elements(self, list_of_elements):
        for element in list_of_elements:
            if element is None:
                break
            self.insert_at_end(element)
        return self

    def generate_list(self, length, start, end):
        for i in range(length):
            self.insert_at_end(randint(start, end))
        return self

    def swap_halves(self):
        result_list = LinkedList()
        half_length = self.size // 2
        for i in range(half_length, self.size):
            element = self[i]
            result_list.insert_at_end(element)
        for i in range(half_length):
            result_list.insert_at_end(self[i])
        return result_list
