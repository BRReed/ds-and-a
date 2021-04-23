from math import floor

class Tree():

    def __init__(self):
        self.min_tree = []
    
    def add_node(self, data):
        self.node = Node(data)
        self.min_tree.append(self.node)
        self.node_index = (len(self.min_tree) - 1)
        self.percolate_up(self.node_index)

    def rem_node(self):
        temp = self.min_tree[0]
        self.swap(0, self.get_last_index())
        self.min_tree.pop()
        self.percolate_down(0)
        return temp

    def percolate_up(self, index):
        if index == 0:
            return
        parent = floor((index - 1) / 2)
        if self.min_tree[parent].data > self.min_tree[index].data:
            self.swap(parent, index)
            self.percolate_up(parent)

    def percolate_down(self, p_index):
        p_data = self.get_node_data(p_index)
        l_child_index = self.get_left_child_index(p_index)
        r_child_index = self.get_right_child_index(p_index)
        if l_child_index == None:
            return
        l_child_data = self.get_node_data(l_child_index)
        if r_child_index == None:
            if l_child_data > p_data:
                self.swap(p_index, l_child_index)
            return
        r_child_data = self.get_node_data(r_child_index)
        if l_child_data > r_child_data:
            if r_child_data < p_data:
                self.swap(p_index, r_child_index)
                self.percolate_down(r_child_index)
        if l_child_data < r_child_data:
            if r_child_data < p_data:
                self.swap(p_index, l_child_index)
                self.percolate_down(l_child_index)

    def swap(self, i1, i2):
        temp = self.min_tree[i1]
        self.min_tree[i1] = self.min_tree[i2]
        self.min_tree[i2] = temp

    def get_last_index(self):
        return (len(self.min_tree) - 1)

    def get_left_child_index(self, index):
        l_child = index * 2 + 1
        if l_child > self.get_last_index():
            return None
        return l_child

    def get_right_child_index(self, index):
        r_child = index * 2 + 2
        if r_child > self.get_last_index():
            return None
        return r_child

    def get_node_data(self, index):
        return self.min_tree[index].data

    def print_tree(self):
        for node in self.min_tree:
            print(node.data)


class Node():
    def __init__(self, data):
        self.data = data

