import gkseg

text = '话说天下大势，分久必合，合久必分'.decode('utf-8')

gkseg.init()

print gkseg.seg(text) #segment the sentence into a list of words

print gkseg.term(text) #extract the important words from the sentence

print gkseg.label(text) #label the sentence

gkseg.destory()
