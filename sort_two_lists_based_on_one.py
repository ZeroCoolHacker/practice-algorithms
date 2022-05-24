x = ['a', 'c', 'e', 'd', 'b']
y = [1, 3, 5, 4, 2]

l1, l2 = zip(*sorted(zip(x,y), reverse=True, key=lambda x: x[0]))
print(l1,l2, sep='\n')