myList = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

def swapNumbers(x):
    return (x[1], x[0])

p = sorted(myList, key=lambda x: (x[1], x[0]))
o = sorted(myList, key=swapNumbers)

print(p)
print(o)