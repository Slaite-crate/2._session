"""
['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
'Hello World Huston we are here' -> 'World Huston we'
"""

myList = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
myTuple = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
myString = 'Hello World Huston we are here'

print(myList[1:5])
print(myList[:3])
print(myList[4:])
print(myList[4:5])
print(myList[::2])
print(myList[::-1])
print(list(myTuple[1:5]))
print("'" + myString[6:21] + "'")