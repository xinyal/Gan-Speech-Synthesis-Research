import codecs

f = open('txt.done.data', 'rb') 
byte_lst = []
try:
    byte = f.read(1)
    while byte != '':
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()

s = ''.join(byte_lst)
s = s.decode('utf-8')

uni_lst = list(s)

res = codecs.open("splitted_mandarin.txt", 'w', 'utf-8')

for char in uni_lst:
    if 19968 <= int(str(hex(ord(char))), 16) <= 40959 or 13312 <= int(str(hex(ord(char))), 16) <= 19903:
        res.write(char)
        res.write(" ")
    else:
        res.write(char)
    
res.close()

