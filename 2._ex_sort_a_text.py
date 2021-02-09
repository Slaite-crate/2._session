vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def sortMyText(str):
    result = ''
    for l in str:
        if l not in vowels:
            result += l
    result = sorted(result)
    return result

def sortMyText2(str):
    result = ''.join([l for l in str if l not in vowels])
    result = sorted(result)
    return result

def sortMyText3(str):
    pass


print('write something: ', end='')
x = input()
print(sortMyText(x))