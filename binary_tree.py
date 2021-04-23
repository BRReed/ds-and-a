

class Tree():

    def __init__(self):
        self.head = Node(None)
        self.node = None

    def add_ele(self, search, data):
        self.search = search
        if self.node == None:
            self.node = Node(data)
        if self.search.data == None:
            self.search = self.node
            self.node = None
            return
        elif self.node.data > self.search.data:
            self.add_ele(self.search.right, 1)
        elif self.node.data < self.search.data:
            self.add_ele(self.search.left, 1)
        
    
    def find_ele(self, data):
        self.data = data
        curr = self.head
        while True:
            if curr == None:
                print(f'element not in tree')
                break
            if self.data > curr.data:
                curr = curr.right
                continue
            elif self.data < curr.data:
                curr = curr.left
                continue
            else:
                print(f'found element: {curr.data}')
                break
                
        


    def reorder(self):
        pass


class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.last = None

