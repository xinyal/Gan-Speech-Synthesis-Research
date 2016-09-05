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
f = open('ganfolk_seg.txt', 'rb') 
byte_lst = []
try:
    byte = f.read(1)
    while byte != '':
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()


# get rid of the first 3 bytes, and turn the byte list to a string
#s = ''.join(byte_lst[-15739:]) # len(byte_lst): 15744
s = ''.join(byte_lst[-18507:]) # len(byte_lst): 18510



# decode the byte string to a utf-8 (unicode) string
s = s.decode('utf-8')

# split the utf-8 string by character.
# uni_lst means unicode_lst
uni_lst = list(s) # len(uni_lst): 9029
print len(uni_lst) # le(uni_lst): 12317



counter = 0
# HAVE TO USE codecs.open('name', 'w', 'utf-8') AND f.write() TO WRITE THE FILE!
# CANNOT USE open('w'), MAY CAUSE ENCODING PROBLEMS

res = codecs.open("romanized_gan.txt", 'w', 'utf-8')

# check every char. if the character is a chinese one, then replace it with its
# jyut-ping pronounciation in the output
for char in uni_lst:
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

res.close()
    


# ------------- Drafts Below ------------- #
# tried to test whether the code interval works to determine whether the input is Chinese character
#print int('4e00',16) <= int(str(hex(ord(uni_lst[14]))), 16) <= int('9fff', 16)

# worked for the humanum one..
#big5code = repr(s.decode('utf-8').encode('big5'))

# WILL CAUSE BOM!!!! HAVE TO USE open('name', 'rb') TO READ IN BYTE
# AND TO DELETE THE FIRST 3 ITEMS IN THE BYTE LIST!!!!
#news = ''.join(codecs.open('selectedwiki4copy.txt', 'r', 'utf-8'))
