from collections import deque

"""
    If using as a queue, use append+popleft
    if using as  stack, use append + pop 
"""
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.popleft()
queue.popleft()

# Rotation can be performed with rotate(x)
queue = deque("abcde")
queue.rotate(1) # right rotation -> eabcd
queue.rotate(-1) # Left rotation -> aabcde


# extend left reverses extend input order
queue.clear()
queue.extendleft("xyz") # -> zyx

# Round Robin Recipe

def round_robin(*iterables):
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            iterators.popleft()

result = round_robin("ABC", "D", "EF")
