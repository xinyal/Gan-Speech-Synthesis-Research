import codecs
import re
import csv 

f = open('set_gan_hakka.txt', 'rb')
byte_lst = []
try:
    byte = f.read(1)
    while byte != '':
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()

# No BOM here
s = ''.join(byte_lst)
s = s.decode('utf-8')

# segmentation
# original length 2269
# now 2268
# But a BOM here. char_lst[0] = u'\ufeff\u8981:'
char_lst = s.split()
char_lst[0] = u'\u8981:' # Remove the BOM


# add a 0 tone to all pronounciations
for i in range(0, len(char_lst)/2):
    if ord(char_lst[2 * i + 1][-1]) > 57:
        char_lst[2 * i + 1] = char_lst[2 * i + 1] + str(0)

# build phoneme lists and sets
# See https://en.wikipedia.org/wiki/Pha%CC%8Dk-fa-s%E1%B9%B3
consonants = ['chh', 'ch', 'ph', 'th', 'kh', 'ph', 'ng', 'p', 't', 'k', 'l', 'm', 'n', 's', 'f', 'v', 'h', 'y']
added_c = ['b', 'g', 'c', 'j', 'w', 'z', 'd']
consonants = consonants + added_c

# 'eu', 'ii', 'aa', 'ou' are added
# no 'uo'
# test leoi
# eoi? ieu? ou?
vowels = ['aa', 'ai', 'au', 'ia', 'iu', 'ie', 'io', 'oa', 'oi', 'oe', 'ou', 'eu', 'ii', 'a', 'i', 'e', 'o', 'u', 'y'] 
coda = ['n', 'm', 'k', 'p', 't', 'ng']

# split them by those most basic phoneme units above

def seg(s):
    news = s[:-1]  
    res = ""

    while len(news) != 0:
        for c in consonants:
            if news.startswith(c):
                res = res + c
                news = news[len(c):]
                if len(news) != 0:
                    res = res + "|"
                else:
                    res = res + '|' + s[-1]
        if len(news) != 0:
            for v in vowels:
                if news.startswith(v):
                    res = res + v
                    news = news[len(v):]
                    if len(news) != 0:
                        res = res + "|"
                    else:
                        res = res + '|' + s[-1]
        if len(news) != 0:
            for c in consonants:
                if news.startswith(c):
                    res = res + c
                    news = news[len(c):]
                    if len(news) != 0:
                        res = res + "|"
                    else:
                        res = res + '|' + s[-1]
    return res



res = {}
#for i in range(0, 100):
for i in range(0, len(char_lst)/2):
    pronounciation = char_lst[2*i + 1]
    #print pronounciation
    res[char_lst[2 * i]] = seg(pronounciation)
    #print seg(pronounciation)
    #print '\r' + '\n'

#for key in res:
#    print len(key)


with open("hakka_dict1.csv", 'w') as f:
    writer = csv.writer(f)
    for key, val in res.items():
        writer.writerow([key.encode('utf-8'), val])
        #writer.writerows(val)

#finally:
#    output.close()
print "finished"

    # remember to add a 0 tone at the end of pronounciation







'''
 ========= draft below ===================
 remove Chinese and English punctuation
 of no use after making the input a dictionary

uni_lst = list(s)
for char in uni_lst:
    if ord(char) >= 12289:
        uni_lst[uni_lst.index(char)] = ""
    if 33 <= ord(char) <= 47:
        uni_lst[uni_lst.index(char)] = ""

# remove data_XXXX index
wholestring = "".join(uni_lst)
wholestring = re.sub("data_[0-9]+", "", wholestring)
'''

# the odd number and the pairs does not align
# original file, [u'\u7d50:', u'kiat', u'chhin5'] has an extra hakka at char_lst[1542]
# search the 'jie' of 'jieba' in the hakka online dic for more info
# probably becuz the website provides the hakka in a wrong format
# ( with the hakka of a word starting with the char being the first result,
#   rather than hakka of the char itself, when the latter is available)
#for c in char_lst:
#    if (':' not in c) & (index % 2 == 0):
#        print c
#        print index
#    index = index + 1
#print ''.join(char_lst[1540:1550])


'''
# add tone 0 to ones that don't have tones
for char in char_lst:
    if ord(char[-1:]) > 57: # safety check, see http://www.asciitable.com/
        char_lst[char_lst.index(char)] = char+str(0)

print char_lst[:20]

print len(char_lst)
char_lst = set(char_lst)
print len(char_lst)
# Segment by Hakka Phonemes





#print wholestring[:1000]
'''
