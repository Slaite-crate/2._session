myList = ['Claus', 'Ib', 'Per', 'Pelle', 'Lars', 'Trine', 'Kaare', 'Anders']

def mySortOfThing(str):
    result = str.lower().find('a')
    if result == -1:
        result = 100
    return result

def mySortOfThing2(str):
    if 'a' in str.lower():
        return True
    return False

print(sorted(myList))
print(sorted(myList, reverse=True))
print(sorted(myList, key=len))
print(sorted(myList, key=lambda x: x[::-1]))
print(sorted(myList, key=mySortOfThing))
print(sorted(myList, key=mySortOfThing2)[::-1])