import codecs
import re
import requests
from lxml import html

s = u'\u5c4b' # a more convenient name made by Max
data = {'ch': s, 'env': 'dbmix', 'mode': 'characters'}
response = requests.post("http://www.iso10646hk.net/jp/database/index.jsp#anchorResult", data=data)
tree = html.fromstring(response.content)
jp = tree.xpath("//table/tr[2]/td[2]/text()") # jp is a list with only the jp string in it
print len(jp)
print jp[0]
