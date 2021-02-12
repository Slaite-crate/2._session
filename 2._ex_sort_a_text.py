vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']

def sortMyText(str):
    result = ''
    for l in str:
        k = l
        if k.lower() not in vowels:
            result += l
    result = sorted(result)
    return result

def sortMyText2(str):
    result = ''.join([l for l in str if l not in vowels])
    result = sorted(result)
    return result

def sortMyText3(str):
    for i in vowels:
        str = str.lower().replace(i,'')
    return sorted(str)


print('write something: ', end='')
x = input()
print(sortMyText3(x))