import re
import codecs
from re import compile as _Re
# use regex
#!/Zinnia/bin/python
# -*- coding: utf-8 -*-


# Tried to use group_words(). Proved not to be useful,
# but learned to search unicode and writing unicode from it, that are useful.
# http://stackoverflow.com/questions/3801431/python-any-way-to-perform-this-hybrid-split-on-multi-lingual-e-g-chinese


# Tried to use split_unicode_chrs(). Proved not to be necessary.
# Not particularly necessary to split Chinese articles by characters in sentences.
# Proabably because it is easier than English, using different punctuation system
# (so that no need to consider acronyms etc. (and thus no need for regex that is too complicated))

# Unicode introduction (Important) #
# http://stackoverflow.com/questions/21808657/what-is-a-unicode-string #

# re is the Regular Expression class.
# re.compile and re.sub are re using compile and sub modules

# Codecs (Important) #
# When read and write Chinese, use codecs.open(), and set the encoding to 'utf-8'
# https://docs.python.org/2/library/codecs.html #
# http://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python 

# Unicode table and search
# http://jrgraphix.net/r/Unicode/2000-206F
# http://www.rikai.com/library/kanjitables/kanji_codes.unicode.shtml
# http://xahlee.info/comp/unicode_index.html

# Other potentially useful links concerning processing raw (chinese) text:
# http://stackoverflow.com/questions/2718196/find-all-chinese-text-in-a-string-using-python-and-regex
# http://stackoverflow.com/questions/36640587/how-to-remove-chinese-punctuation-in-python
# http://stackoverflow.com/questions/21209024/python-regex-remove-all-punctuation-except-hyphen-for-unicode-string


codecs.encode("utf8")
def group_words(s): #http://stackoverflow.com/questions/3801431/python-any-way-to-perform-this-hybrid-split-on-multi-lingual-e-g-chinese
    regex = []

    # Match a whole word:
    regex += [ur'\w+']

    # Match a single CJK character:
    regex += [ur'[\u4e00-\ufaff]']

    # Match one of anything else, except for spaces:
    regex += [ur'[^\s]']

    regex = "|".join(regex)
    r = re.compile(regex)

    return r.findall(s)

def find_punc(s):
    regex = []
    regex += [ur'[\u3002]']
    regex += [ur'[\uff01]']
    regex += [ur'[\uff1b]']

    regex = "|".join(regex)
    r = re.compile(regex)

    return r.findall(s)


# http://stackoverflow.com/questions/3797746/how-to-do-a-python-split-on-languages-like-chinese-that-dont-use-whitespace
from re import compile as _Re
_unicode_chr_splitter = _Re( '[\u3002]|[\uff01]|[\uff1b]' ).split
def split_unicode_chrs(text):
    return [ chr for chr in _unicode_chr_splitter(text) if chr ]


text = ''.join(open('wiki_test').readlines()) # in lines
text = re.split('\n', text)

def cleardoc(text):
    newtext = "" # in letters
    for paragraph in text:
        paragraph = "".join(group_words(paragraph))
        paragraph = paragraph + '\n'
        newtext += paragraph

    docpattern = "(<)"+ "(.?doc\s?\w?)" + "(>)"
    
    nodoc = "" # in letter...

    for line in text:
        nodoc += re.sub(docpattern, "", line)
        nodoc += '\n'
    nodoc = "".join(nodoc)
    nodoc = re.split('\n', nodoc) # a large no <\doc> chunk
    return nodoc

nodoc = cleardoc(text) # in lines


def clearurl(nodoc):
    urlpattern = "(<doc)" + ".+" + "(>)"

    nourl = ""
    
    for line in nodoc:
        nourl += re.sub(urlpattern, "", line)
        nourl += '\n'
    nourl = "".join(nourl)
    nourl = re.split('\n', nourl)
    return nourl

nourl = clearurl(nodoc)

# write a clean text
#cleantext = open('cleanwiki_0.txt', 'w')
#for line in nourl:
#    cleantext.write(line)
#    cleantext.write('\n')
#cleantext.close()


letters = "".join(nourl)
# does not seem to matter
#chrs = group_words(letters)


chrs = ""
#for letter in letters:
#    chrs += letter

for line in nourl:
    chrs += line
    chrs += '\n'

#chrlist = split_unicode_chrs(chrs)
#chrlist[50].decode("UNICODE")
#print chrlist[:100]
    
#print chrs[:100]

chrssplit = list(chrs)
print chrssplit[:5]

def sub_punc(chrs):
    #chrs = re.sub(unichr(3002).decode('utf8'), "".decode('utf8'),chrs)
    RE = re.compile(u'\u3002', re.UNICODE)
    res = RE.sub('\n', chrs)
    return res

#def print_punc(chrs):
#    for n in re.findall(ur)

    
def split_punc(chrs):
    regex = []
    #regex += ['¡£'.decode("utf8")]
    regex += [ur'[\u4e00 - \u4f00]']
    regex += [ur'[\u3002]']
    #regex += [ur'[\uff01]']
    #regex += [ur'[\uff1b]']

    regex = "|".join(regex)

    res = ""

    r = re.compile(regex)

    return r.findall(chrs)
    res = re.sub(regex, "\n", chrs)
    #for char in chrs:
        #print re.sub(regex, "\n", char)
    #    res = re.sub(regex, "", chrs)
    #    res += '\n'
    #res = "".join(res)
    #res = re.split('\n', res)
    return res

res = sub_punc(chrs)

print res[1000:2000]
#print res[:1000]




#print res[56]
#print res[:2000]
#for i in range(1,50):
#    print res[i]
    #for line in text:
        
    #for match in r.finditer(text):
        

        
#res = ""
#for line in newtext:
    #line = line.decode("utf8")
#    line = re.sub("[¡££¿£¡£»]+", '\n', line)
#    res = res + line
    #line = re.sub("[¡££¿£¡£»]+".decode("utf8"), '\n'.decode("utf8"), line)

#print res[:1000]
#target = open('utf8split_wiki-groupwords.txt', 'w')

#target.write("".join(group_words(res)))
#target.write("\n")

#target.close()
