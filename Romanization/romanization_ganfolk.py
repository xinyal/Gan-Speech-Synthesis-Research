import codecs
import re
import requests
from lxml import html

# the iso10646hk.net provides the jyutping string with its audio link.
# Max uses the xpath method that can locate a link in a page to get the jp string 
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


# read in bytes to get the byte list of the file
# and then get rid of the first 3 items, which are the BOM
# THE FILE HAS TO BE ENCODED IN UTF-8 FOR THIS TO WORK, NOT ANSI
f = open('ganfolk_seg.txt', 'rb') # 18478
byte_lst = []
try:
    byte = f.read(1)
    while byte != '':
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()

print len(byte_lst)

# get rid of the first 3 bytes, and turn the byte list to a string
s = ''.join(byte_lst[-18475:]) # len(byte_lst): 18478

# decode the byte string to a utf-8 string
s = s.decode('utf-8')

# split the utf-8 string by character
uni_lst = list(s) # len(uni_lst): 9029


#output_lst = []
counter = 0

res = codecs.open("romanized_ganfolk.txt", 'w', 'utf-8')

# check every char. if the character is a chinese one, then replace it with its
# jyut-ping pronounciation in the output
for char in uni_lst[:55]:
    print counter
    #print "start of loop:" + char
    if 19968 <= int(str(hex(ord(char))), 16) <= 40959 or 13312 <= int(str(hex(ord(char))), 16) <= 19903:
        #print "ord is "
        #print int(str(hex(ord(char))), 16)
        #print "to getjp"
        jp = getjp(char)
        res.write(jp)
        #output_lst.append(jp)
    else:
        #print "directly written"
        #output_lst.append(char)
        res.write(char)
    
    counter += 1

#res = open("romanized_wiki4sent.txt", 'w')
#res = codecs.open("romanized_wiki4sent.txt", 'w', 'utf-8')
#res.write(''.join(output_lst))
res.close()
