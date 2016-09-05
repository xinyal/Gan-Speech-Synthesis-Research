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

def write_word(s):
    s = s.split()
    print len(s)
    print len(set(s))
    for i in range(0, 21):
        print s[i]


s = read_check_bom("word_list_notset.txt")
write_word(s)
