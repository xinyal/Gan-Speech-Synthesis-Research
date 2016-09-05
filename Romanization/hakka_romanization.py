import codecs
import re
import requests
from lxml import html


# http://hakka.fhl.net/dict/index_hakka.html provides

def getjp(character):
    s = character # a more convenient name made by Max
    data = {'ch': s, 'env': 'dbmix', 'mode': 'characters'}
    response = requests.post("http://www.iso10646hk.net/jp/database/index.jsp#anchorResult", data=data)
    tree = html.fromstring(response.content)
    jp = tree.xpath("//table/tr[2]/td[2]/a/text()") # jp is a list with only the jp string in it
    #print len(jp)
    if len(jp) == 0:
        jp = tree.xpath("//table/tr[2]/td[2]/text()") # if there is no link to the jp
    res = jp[0]
    
    return res

def gethakka(character):
    s = character # a more convenient name made by Max

    data= {"ckey":s}
    #data = {"ckey": repr(u'\u99ac'.encode('utf-8'))}
    #data = {"ckey":"\xe9\xa6\xac"}
    response = requests.post("http://hakka.fhl.net/dict/search_hakka.php", data = data)
    tree = html.fromstring(response.content)
    hakka = tree.xpath("/html/body/table[2]/tr[2]/td[2]/text()")
    if len(hakka) != 0:
        #print hakka[0][:-1]
        #res = hakka[0]
        res = hakka[0][:-1]
        if "-" in res:
            return res[:res.index("-")]
        return res
    else:
        res = getjp(s)
        #print res
        return res
    #for table in tree.iter('table'):
    #    print table.tag, table.attrib
    #    for subdir in table:
    #        print subdir.tag, subdir.attrib

f = open('txt.done.data', 'rb') 
byte_lst = []
try:
    byte = f.read(1)
    while byte != '':
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()
#len(byte_lst) = 31126


# -15741, full wiki
# -18507, Full folk
s = ''.join(byte_lst) # Removed the BOM

s = s.decode('utf-8')

# split the utf-8 string by character.
# uni_lst means unicode_lst
uni_lst = list(s)

#test = uni_lst[23]
#print test

#print repr(test)
#print u'\u55f0'

#gethakka(u'\u55f0')

counter = 0

res = codecs.open("hakka_data.txt", 'w', 'utf-8')

for char in uni_lst:
    print counter
    #print "start of loop:" + char
    if 19968 <= int(str(hex(ord(char))), 16) <= 40959 or 13312 <= int(str(hex(ord(char))), 16) <= 19903:
        #print "ord is "
        #print int(str(hex(ord(char))), 16)
        #print "to getjp"
        hakka = gethakka(char)
        res.write(hakka)
        #output_lst.append(jp)
    else:
        #print "directly written"
        #output_lst.append(char)
        res.write(char)
    
    counter += 1

res.close()

