class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left: Node = left
        self.right: Node = right
    
    def __repr__(self):
        return self.value
        

    def breadth_first_traversal(self):
        queue = [self]
        results = []
        while queue:
            current = queue.pop(0)
            results.append(current.value)
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        return results
    
    

d = Node('d')
e = Node('e')
b = Node('b', left=d, right=e)
f = Node('f')
c = Node('c', right=f)
a = Node('a', left=b, right=c)

print(a.breadth_first_traversal())