

class InsertionSort():

    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        if self.get_data(node) < self.get_data(self.head):
            node.next = self.head
            self.head = node
            return
        self.insert(node, self.head)
    
    def insert(self, node, compare):
        if compare.next == None:
            self.swap(node, compare)
            return
        if ((self.get_data(node) < self.get_data(compare.next)) or (
            self.get_data(node) == self.get_data(compare.next))
            ):
            self.swap(node, compare)
            return
        self.insert(node, compare.next)

    def swap(self, node, compare):
        node.next = compare.next
        compare.next = node

    def get_data(self, node):
        return node.data

    def is_empty(self):
        return self.head == None
    
    def arr_sort(self, a):
        t = InsertionSort()
        for n in a:
            t.add(n)
        return t

    def print_nodes(self):
        n = self.head
        while n != None:
            print(n.data)
            n = n.next


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

