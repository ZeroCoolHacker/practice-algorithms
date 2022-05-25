x = [15, -4, 56, 10, -23]
y = [14, -9, 56, 14, -23]

def calculate_absolute_difference(x, y):
    if not x or not y:
        return 0
    first, second = x.pop(), y.pop()
    diff = abs(first - second)
    return diff + calculate_absolute_difference(x, y)

print(calculate_absolute_difference(x, y))