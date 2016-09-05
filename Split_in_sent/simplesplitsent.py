import re
from re import compile as _Re
# use regex

# Tried directly re.sub() and used regex to extract all Chinese sentences
# The basic thinking of direct substitution is right







def split_unicode_chrs(text):
    return [ chr for chr in _unicode_chr_splitter(text) if chr ]


text = ''.join(open('wiki_test').readlines())
print text[:10]
sentences = re.split(r' *[\¡£\£¿£¡][\'"¡°¡±¡®¡¯\)\]]* *', text)
#print sentences[:50]
target = open('split_wiki.txt', 'w')
_unicode_chr_splitter = _Re( '(?s)((?:[\ud800-\udbff][\udc00-\udfff])|.)' ).split

for each in sentences:
    spliteachchr = split_unicode_chrs(each)
    sent = "".join(spliteachchr)
    target.write(sent)
    target.write("\n")
target.close()

#import nltk.data

#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#fp = open("wiki_test")
#data = fp.read()
#print '\n-----\n'.join(tokenizer.tokenize(data))
