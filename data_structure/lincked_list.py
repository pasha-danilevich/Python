class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        
    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end

linked_list = Node(10)

linked_list.append(20)
linked_list.append(30)

node = linked_list

print(node.data)
while node.next:
    node = node.next
    print(node.data)