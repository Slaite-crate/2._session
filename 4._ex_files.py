f = open('songs.docx', 'w')
f.writelines('hello\nmy old\nfriend')
f.close()

f = open('songs.docx', 'r')
f = f.read()
print(f)

f = open('songs.docx', 'r')
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()

print()

f = open('songs.docx', 'r')
for i in f.readlines():
    print(i, end='')

print()
