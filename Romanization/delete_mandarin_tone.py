import codecs
import re


f = codecs.open('mandarin_toned_data.txt', 'rb')
byte_lst = []

try:
    byte = f.read(1)
    while byte != '':
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()

print byte_lst[:5]
print len(byte_lst)
byte_lst = byte_lst[-35060:]
s = ''.join(byte_lst)
print s[-1]

# no BOM

s = s.lower()
s = s.decode('utf-8')
uni_lst = list(s)

'''
for e in [275, 233, 283, 232]:
    s = re.sub(unichr(e), "e", s)

# third
for i in [299, 237, 464, 236]:
    s = re.sub(unichr(i), "i", s)

for a in [257, 225, 462, 224]:
    s = re.sub(unichr(a), "a", s)

for u in [363, 250, 468, 249]:
    s = re.sub(unichr(u), "u", s)

for o in [333, 243, 466, 242]:
    s = re.sub(unichr(o), "o", s)

for y in [470, 472, 474, 476]:
    s = re.sub(unichr(y), unichr(252), s)
'''

#output = ""

res = codecs.open('mandarin_toned.done.data', 'w', 'utf-8')
for char in s:
    if ord(char) <= 41:
        if ord(char) <= 32 or ord(char) == 34 or 39 < ord(char) <= 41:
            #output.append(char)
             res.write(char)
    if 48 <= ord(char) <= 57:
        #output.append(char)
        res.write(char)
    if ord(char) == 95:
        res.write(char)
    if ord(char) >= 97:
        #output.append(char)
        res.write(char)



#res.close()
#s1 = unicode(s1, 'cp775')
#print s1[10:15]
#uni_lst = list(s1)
#print uni_lst[10:15]

#s1 = s1.decode('cp775')
#s1 = unicode(s1, 'cp775')
#s1 = unichr(s1)

#print re.match(unichr(237), s1)
#s1 = re.sub(unichr(237), 'i', s1)
#print s1[:20]

#res = codecs.open('mandarin_data.txt', 'w', 'cp775')
#for char in s1[:30]:
#    res.write(char)
#res.close()



'''
s1 = s1.decode('cp775')
s1lst = list(s1)

print s1lst[10:15]
'''





# since the mandarin pinyin offered by Google Translate
# represents tone directly by printing out the toned character,
# e.g. ā, like a chinese character, the length of ā is greater than 1;
# thus, identify all the items of length greater than 1 to identify tones.

#print uni_lst[12:16]

'''
counter = 0
for char in byte_lst:
    if len(char) > 1:
        print char
    print counter
    counter += 1
'''
