import codecs
import re
import requests
from lxml import html

def tone(character):
    s = character

    url1 = "http://ytenx.org/zim?dzih="
    url2 = "&dzyen=1&jtkb=1&jtdt=1"
    response = requests.get(url1 + s + url2)    
    
    tree = html.fromstring(response.content)
    #print len(response.content)

    res = tree.xpath("//div/p[1]/a[1]/text()")
    #res = tree.xpath("//div/p")
    '''
    for href in tree.iter('href'):
        print href.attrib
    for element in res:
        print element.tag
    '''
    print ''.join(res)

tone(u'\u4e00')
