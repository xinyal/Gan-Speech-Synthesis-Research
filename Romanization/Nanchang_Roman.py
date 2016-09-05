import codecs
import re
import requests
import urllib2
from lxml import html


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

def get_hakka(character):
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



def getdialect(character):
    s = character
    
    url1 = 'http://starling.rinet.ru/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cchina%5Cdoc&first=1&off=&text_character=&method_character=substring&ic_character=on&text_mcinfo=&method_mcinfo=substring&ic_mcinfo=on&text_zihui=&method_zihui=substring&ic_zihui=on&text_beijing=&method_beijing=substring&ic_beijing=on&text_jinan=&method_jinan=substring&ic_jinan=on&text_xian=&method_xian=substring&ic_xian=on&text_taiyuan=&method_taiyuan=substring&ic_taiyuan=on&text_hankou=&method_hankou=substring&ic_hankou=on&text_chengdu=&method_chengdu=substring&ic_chengdu=on&text_yangzhou=&method_yangzhou=substring&ic_yangzhou=on&text_suzhou=&method_suzhou=substring&ic_suzhou=on&text_wenzhou=&method_wenzhou=substring&ic_wenzhou=on&text_changsha=&method_changsha=substring&ic_changsha=on&text_shuangfeng=&method_shuangfeng=substring&ic_shuangfeng=on&text_nanchang=&method_nanchang=substring&ic_nanchang=on&text_meixian=&method_meixian=substring&ic_meixian=on&text_guangzhou=&method_guangzhou=substring&ic_guangzhou=on&text_xiamen=&method_xiamen=substring&ic_xiamen=on&text_chaozhou=&method_chaozhou=substring&ic_chaozhou=on&text_fuzhou=&method_fuzhou=substring&ic_fuzhou=on&text_shanghai=&method_shanghai=substring&ic_shanghai=on&text_zhongyuan=&method_zhongyuan=substring&ic_zhongyuan=on&text_any='
    url2 = '&method_any=substring&sort=number&ic_any=on'
    response = requests.get(url1 + s + url2)
    
    tree = html.fromstring(response.content)
    print len(response.content)
    res = tree.xpath("//div[contains(span, 'Nanchang:')]/span[2]/text()")
    print len(res)

    if len(res) > 1:
        res = get_hakka(s)
        print res
        return res
    
    # Shouldn't print res[0].encode('utf-8'). Will probably results on wrong characters.
    #print ''.join(list(res[0]))
    res = ''.join(list(res[0]))

    # Sigh...
    # If there are multiple pronounciation of the character
    # Choose the first one...
    if ';' in res:
        res = re.sub('[A-Z]:', '', res)
        #print res
        res = res[1:res.index(';')]
    print res
    return res
       


# print (u'/u91cd'.encode('utf-8'))
# encode to utf-8 and then byte???
# For this website and the hakka one, just use the character
# aka, u'\uXXXX'
f = open('txt.done.data', 'rb')
byte_lst = []
try:
    byte = f.read(1)
    while byte != '':
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()

# No BOM
s = ''.join(byte_lst) 
s = s.decode('utf-8')
uni_lst = list(s)

counter = 0
res = codecs.open('nanchang_toned.done.data', 'w', 'utf-8')
for char in uni_lst:
    print counter
    if 19968 <= int(str(hex(ord(char))), 16) <= 40959 or 13312 <= int(str(hex(ord(char))), 16) <= 19903:
        nanchang = getdialect(char)
        res.write(nanchang)
    else:
        res.write(char)

    counter += 1





getdialect(u'\u55f0')
getdialect(u'\u91cd')
getdialect(u'\u6211')


#print char

#url1 = 'http://starling.rinet.ru/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cchina%5Cdoc&first=1&off=&text_character=&method_character=substring&ic_character=on&text_mcinfo=&method_mcinfo=substring&ic_mcinfo=on&text_zihui=&method_zihui=substring&ic_zihui=on&text_beijing=&method_beijing=substring&ic_beijing=on&text_jinan=&method_jinan=substring&ic_jinan=on&text_xian=&method_xian=substring&ic_xian=on&text_taiyuan=&method_taiyuan=substring&ic_taiyuan=on&text_hankou=&method_hankou=substring&ic_hankou=on&text_chengdu=&method_chengdu=substring&ic_chengdu=on&text_yangzhou=&method_yangzhou=substring&ic_yangzhou=on&text_suzhou=&method_suzhou=substring&ic_suzhou=on&text_wenzhou=&method_wenzhou=substring&ic_wenzhou=on&text_changsha=&method_changsha=substring&ic_changsha=on&text_shuangfeng=&method_shuangfeng=substring&ic_shuangfeng=on&text_nanchang=&method_nanchang=substring&ic_nanchang=on&text_meixian=&method_meixian=substring&ic_meixian=on&text_guangzhou=&method_guangzhou=substring&ic_guangzhou=on&text_xiamen=&method_xiamen=substring&ic_xiamen=on&text_chaozhou=&method_chaozhou=substring&ic_chaozhou=on&text_fuzhou=&method_fuzhou=substring&ic_fuzhou=on&text_shanghai=&method_shanghai=substring&ic_shanghai=on&text_zhongyuan=&method_zhongyuan=substring&ic_zhongyuan=on&text_any='
#url2 = '&method_any=substring&sort=number&ic_any=on'
#print url1+char+url2

#response = requests.post(url1+char+url2)
#tree = html.fromstring(response.content)
#print url1+char+url2

#for child in tree:
#    print child.tag, child.attrib
#    for grandchild in child:#
        #print child.tag, child.attrib




#char = re.match('\W', '%', repr(u'\u91cd'.encode('utf-8')))
#char = re.sub('\\\\', r'%', repr(u'\u91cd'.encode('utf-8')))[:-1]
#print char
#char = u'\u91cd'


#print tree.xpath('body/text()')
