import codecs
import re
import csv
import itertools

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

# Mutiply nasalizing consonants to nasalizable vowels
# to get a list of nasalized vowels
nasalizable_v = ['a', 'i', 'ii', 'e', 'o', 'u', 'ai', 'au', 'ia', 'iu', 'ie', 'io', 'oa', 'oi', 'oe', 'eu']
nasalize = ['ng', 'm', 'n', 'p', 't', 'k']
product = itertools.product(nasalizable_v, nasalize)
product = list(product)
nasalized_vowels = []
for pair in product:
    nasalized_vowels.append(''.join(pair))


#print nasalized_vowels
vowels = ['ai', 'au', 'ia', 'iu', 'ie', 'io', 'oa', 'oi', 'oe', 'eu', 'ii', 'a', 'i', 'e', 'o', 'u', 'y']
vowels = nasalized_vowels + vowels
#print vowels

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
for i in range(0, 100):
#for i in range(0, len(char_lst)/2):
    pronounciation = char_lst[2*i + 1]
    print pronounciation
    res[char_lst[2 * i]] = seg(pronounciation)
    print seg(pronounciation)
    print '\r' + '\n'

#for key in res:
#    print len(key)

'''
with open("hakka_nasalized_dict.csv", 'w') as f:
    writer = csv.writer(f)
    for key, val in res.items():
        writer.writerow([key.encode('utf-8'), val])
        #writer.writerows(val)

#finally:
#    output.close()
print "finished"
'''
