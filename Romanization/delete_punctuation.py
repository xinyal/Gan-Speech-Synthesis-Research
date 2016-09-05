import codecs
import re

f = open("cantonese_data.txt", 'rb')
byte_lst = []

try:
    byte = f.read(1)
    while byte != "":
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()

# cantonese_data length:32293

# check if the first 3 items are BOM.
# BOM in bytes is []'\xef', '\xbb', '\xbf']

# So there is BOM. Delete the first 3 items.
# len(byte_lst) is 17916
#byte_lst = byte_lst[-17913:]

# join the list to string to delete punctuation.
s = "".join(byte_lst)


# decode the byte string to a utf-8 (unicode) string
s = s.decode('utf-8')

'''
s = re.sub("(?<![0-9_])[0-9] ", ' ', s)
s = re.sub("[0-9](?=[a-z])", "", s)
s = re.sub("[0-9](?=[\"])", "", s)


#s = re.sub('(?!data_)[0-9]', '', s)
uni_lst = list(s)
res = codecs.open('hakka_data_no_tone.txt', 'w', 'utf-8')

counter = 0
for char in uni_lst:
    print counter
    res.write(char)
    counter += 1
res.close()
'''


# split the utf-8 string by character.
# uni_lst means unicode_lst
uni_lst = list(s) # len(uni_lst) is 17601

counter = 0
res = codecs.open('cantonese_data_no_punc.txt', 'w', 'utf-8')

for char in uni_lst:
    print counter
    # the second to last item in the ascii table
    if int(str(hex(ord(char))), 16) <= 126:
        res.write(char)
    counter += 1
res.close()


