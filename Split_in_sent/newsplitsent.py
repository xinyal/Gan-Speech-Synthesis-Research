import re
import codecs
from re import compile as _Re

# -*- coding: utf-8 -*-


text = ''.join(codecs.open('wiki_00', 'r', 'utf-8'))
text = re.split('\n', text)

#http://stackoverflow.com/questions/3801431/python-any-way-to-perform-this-hybrid-split-on-multi-lingual-e-g-chinese
def group_words(s): 
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

# clear <\doc>
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


# wiki doc cleared of <\doc>
nodoc = cleardoc(text) # in lines (type: list)


# clear all urls
def clearurl(nodoc):
    urlpattern = "(<doc)" + ".+" + "(>)"

    nourl = ""
    
    for line in nodoc:
        nourl += re.sub(urlpattern, "", line)
        nourl += '\n'
    nourl = "".join(nourl)
    nourl = re.split('\n', nourl)
    return nourl


# wiki doc of articles only
nourl = clearurl(nodoc) # type: list


# change the nourl to a string
chrs = ""
for line in nourl:
    chrs += line
    chrs += '\n'


# split the wiki doc string in sentences
def split_punc(chrs):
    regex = []

    regex += [ur'[\u3002]'] # period
    regex += [ur'[\uff1b]'] # semicolon
    regex += [ur'[\uff01]'] # exclamation

    regex = "|".join(regex)

    res = ""

    r = re.compile(regex)

    res = re.sub(regex, "\n", chrs)
    
    return res

# Wiki doc splitted in sentences, a string
res = split_punc(chrs)


# Write to a file
target = codecs.open('wiki_00_sent', 'w', 'utf-8')
for char in res:
    target.write(char)
target.close()

