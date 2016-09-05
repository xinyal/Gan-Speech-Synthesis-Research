import re
from re import compile as _Re
# use regex
# -*- coding: utf-8 -*-

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

def split_unicode_chrs(text):
    return [ chr for chr in _unicode_chr_splitter(text) if chr ]


text = ''.join(open('wiki_test').readlines())
print text[:10]
sentences = re.split(r' *[\¡£\£¿£¡][\'"¡°¡±¡®¡¯\)\]]* *', text)
#print sentences[:50]
target = open('utf8split_wiki.txt', 'w')
_unicode_chr_splitter = _Re( '(?s)((?:[\ud800-\udbff][\udc00-\udfff])|.)' ).split

for each in sentences:
    spliteachchr = group_words(each)
    sent = "".join(spliteachchr)
    target.write(sent)
    target.write("\n")
target.close()

#import nltk.data

#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#fp = open("wiki_test")
#data = fp.read()
#print '\n-----\n'.join(tokenizer.tokenize(data))
