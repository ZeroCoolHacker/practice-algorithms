class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left: Node = left
        self.right: Node = right
        

    def depth_first_traversal(self):
        stack = [self]
        results = []
        while stack:
            current = stack.pop()
            results.append(current.value)

            if current.right: stack.append(current.right)
            if current.left: stack.append(current.left)
        return results

d = Node('d')
e = Node('e')
b = Node('b', left=d, right=e)
f = Node('f')
c = Node('c', right=f)
a = Node('a', left=b, right=c)

a.depth_first_traversal()

def another_depth_first_way(root: Node):
    if not root:
        return []
    left = root.left.depth_first_traversal()
    right = root.right.depth_first_traversal()
    return [root.value, *left, *right]
print(another_depth_first_way(a))