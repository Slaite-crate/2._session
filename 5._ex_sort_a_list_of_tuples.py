myList = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

p = sorted(myList, key=lambda x: (x[1], x[0]))

print(p)