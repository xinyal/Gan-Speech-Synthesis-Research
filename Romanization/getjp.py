import codecs
import urllib2
import re


#response = urllib2.urlopen('http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q=%B6%AE')
#f = open('resultpageenc.txt', 'w')

#response = urllib2.urlopen('http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q=%A4%B8')
#f = open('resultpageencyun.txt', 'w')

response = urllib2.urlopen('http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q=%A8%B0')
f = open('resultpageyut.txt', 'w')

#print response.read()
lst = response.readlines()
#f.write(''.join(lst).decode('big5').encode('utf-8'))
s = ''.join(lst).decode('big5').encode('utf-8')



m = re.search('(?<=<td align=center><a href=\"sound.php)\S+', s)
#m = re.search('(<td align=center><a href=\"sound.php?s=)\s+(target=sound><img)', s)
print m.group(0)
jp = m.group(0)
jp = re.sub('s=', '', jp)
print re.search('\w+', jp).group(0)
#print re.sub(r'?', '', jp)


#print m.group(1)
#print m.group(2)
#for line in lst:
#    m = re.search('(<td align=center><a href=\"sound.php?s=)\s+', line)
#    if m is not None:
    #if m.group(0) != '':
#        print line
#        print m.group(0)
#        jp = m.group(0)
#print jp
    
            
                  
                  
#print codecs.open('http://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q=%B6%AE', 'utf-8').read()
