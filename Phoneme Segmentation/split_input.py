import codecs
import sys
import requests
from lxml import html
import re

def getjp(character):
    s = character # a more convenient name made by Max
    data = {'ch': s, 'env': 'dbmix', 'mode': 'characters'}
    response = requests.post("http://www.iso10646hk.net/jp/database/index.jsp#anchorResult", data=data)
    tree = html.fromstring(response.content)
    jp = tree.xpath("//table/tr[2]/td[2]/a/text()") # jp is a list with only the jp string in it
    if len(jp) == 0:
        jp = tree.xpath("//table/tr[2]/td[2]/text()") # if there is no link to the jp
    res = jp[0]

    return res

def gethakka(character):
    s = character # a more convenient name made by Max

    data= {"ckey":s}

    response = requests.post("http://hakka.fhl.net/dict/search_hakka.php", data = data)
    tree = html.fromstring(response.content)
    hakka = tree.xpath("/html/body/table[2]/tr[2]/td[2]/text()")
    if len(hakka) != 0:
        res = hakka[0][:-1]
        if "-" in res:
            return res[:res.index("-")]
        return res
    else:
        res = getjp(s)
        return res

#f = open(sys.argv[1], 'rb')
f = open("gan_all.txt", 'rb')
byte_lst = []
try:
    byte = f.read(1)
    while byte != '':
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()

l = 3 - len(byte_lst)
s = ''.join(byte_lst[l:])
s = s.decode('utf-8')

uni_lst = list(s)
print "list length: " + str(len(uni_lst))
print ''.join(uni_lst[:200])
uni_lst = set(uni_lst)
print "set length: " + str(len(uni_lst))



counter = 0

res = codecs.open("set_gan_hakka.txt", 'w', 'utf-8')

for char in uni_lst:
    print counter
    #print "start of loop:" + char
    if 19968 <= int(str(hex(ord(char))), 16) <= 40959 or 13312 <= int(str(hex(ord(char))), 16) <= 19903:
        #print "ord is "
        #print int(str(hex(ord(char))), 16)
        #print "to getjp"
        hakka = gethakka(char)
        res.write(char+": "+hakka+'\r'+'\n')
        #res.write('\r' + '\n')
        #res.write("\n")
        #output_lst.append(jp)
    #else:
        #print "directly written"
        #output_lst.append(char)
        #res.write(char)

    counter += 1

res.close()
