from collections import deque


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left: Node = left
        self.right: Node = right
    
    def __bool__(self):
        return self.value != None
    
    def __repr__(self) -> str:
        return self.value
    
    def __iter__(self):
        stack = [self]
        while stack:
            current = stack.pop()
            yield current
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                
        
    
    def depth_first_operation(self, operation=None):
        assert operation, "No operation provided"
        if not self:
            return None
        operation(self)
        if self.left:
            self.left.depth_first_operation(operation)
        if self.right:
            self.right.depth_first_operation(operation)

    def depth_first_list(self, results=[]):
        left = []
        right = []
        if not self:
            return None
        if not results:
            results = [self.value]
        if self.left:
            left = self.left.depth_first_list()
        if self.right:
            right = self.right.depth_first_list()
        return results + left + right
    
    def breadth_first_operations(self, operation=None):
        if not self:
            return
        current = self 
        queue = deque()
        queue.append(self)
        while queue:
            current = queue.popleft()
            operation(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

d = Node('d')
e = Node('e')
b = Node('b', left=d, right=e)
f = Node('f')
c = Node('c', right=f)
a = Node('a', left=b, right=c)
a.depth_first_operation(operation=print)
a.depth_first_list()
a.breadth_first_operations(operation=print)
print(list(a))
for x in a:
    print(x)