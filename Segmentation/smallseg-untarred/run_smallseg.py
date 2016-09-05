#encoding=utf-8
#import psyco
#psyco.full()

import codecs
from smallseg import SEG
seg = SEG()


def cuttest(text):
    wlist = seg.cut(text)
    wlist.reverse()
    tmp = " ".join(wlist)
    print tmp
    print "================================"
        
if __name__=="__main__":
    text = ''.join(open('wiki_test', 'r'))
    cuttest(text)
