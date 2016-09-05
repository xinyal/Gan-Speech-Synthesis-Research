import codecs
import csv
import requests
import re
from lxml import html

def read_check_bom(filename):
    f = open(filename, "rb")
    byte_lst = []
    try:
        byte = f.read(1)
        while byte != '':
            byte_lst.append(byte)
            byte = f.read(1)
    finally:
        f.close()

    s = ""
    if byte_lst[0] == '\xef' and byte_lst[1] == '\xbb' and byte_lst[2] == '\xbf':
        len_kept = 3 - len(byte_lst) # keep all chars after the first 3 BOM
        s = ''.join(byte_lst[len_kept:])
        s = s.decode('utf-8')
    else:
        s = ''.join(byte_lst)
        s = s.decode('utf-8')
    print "Open file length"
    print len(s)
    return s


def exclude_non_chinese(s):
    exclude = []
    for i in range(33, 128):
        exclude.append(chr(i))
    chinese_punc = [u'\u3000', u'\u3001', u'\u3002', u'\u3008', u'\u3009', u'\u300a', u'\u300b', u'\u300c', u'\u300d', u'\u300e', u'\u300f',
                    u'\u3010', u'\u3011', u'\u301d', u'\u301e', u'\uff01', u'\uff02', u'\uff03', u'\uff04', u'\uff05', u'\uff06', u'\uff07',
                    u'\uff08', u'\uff09', u'\uff0c', u'\uff0f', u'\uff1a', u'\uff1b', u'\uff1f', u'\uff3b', u'\uff3d', u'\uff0d']
    exclude = exclude + chinese_punc
    exclude = set(exclude)
    print "before deleting punc"
    print len(s)
    s = ''.join(ch for ch in s if ch not in exclude)
    print "after deleting punc"
    print len(s)
    return s

def write_word(s):
    word_list = s.split()
    #len(s)
    #word_list = set(word_list)

    print len(word_list)

    counter = 0
    res_name = "word_list_notset.txt"
    res = codecs.open(res_name, 'w', 'utf-8')
    for word in word_list:
        print counter
        res.write(word)
        res.write("\r\n")
        counter += 1
    res.close()




s = read_check_bom("txt.done.data")
s = exclude_non_chinese(s)
write_word(s)
