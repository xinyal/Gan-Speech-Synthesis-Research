import codecs

f = open('gan_test.txt', 'rb')
byte_lst = []

try:
    byte = f.read(1)
    while byte != '':
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()

print len(byte_lst)
print byte_lst[:5]
byte_lst = byte_lst[-2262:]
print byte_lst[:5]

s = ''.join(byte_lst)
s = s.decode('utf-8')

res = codecs.open('gan.test.data', 'w', 'utf-8')
for char in s:
    res.write(char)
res.close()

    
