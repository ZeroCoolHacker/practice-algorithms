def isValid(string):
    open_close_map = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for s in string:
        print(stack)
        if s in ('(', '{', '['):
            stack.append(s)
        elif s in (')', '}', ']'):
            if s == open_close_map[stack[-1]]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


result = isValid("()[]{}")
if result:
    print("Valid")
else:
    print("Invalid")