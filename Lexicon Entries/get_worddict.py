import codecs
import csv
import requests
import re
from lxml import html

def getjp(character):
    s = character # a more convenient name made by Max
    data = {'ch': s, 'env': 'dbmix', 'mode': 'characters'}
    response = requests.post("http://www.iso10646hk.net/jp/database/index.jsp#anchorResult", data=data)
    tree = html.fromstring(response.content)
    jp = tree.xpath("//table/tr[2]/td[2]/a/text()") # jp is a list with only the jp string in it
    if len(jp) == 0:
        jp = tree.xpath("//table/tr[2]/td[2]/text()") # if there is no link to the jp
    res = jp[0]
    return res


def gethakka(character):
    s = character # a more convenient name made by Max
    data= {"ckey":s}
    response = requests.post("http://hakka.fhl.net/dict/search_hakka.php", data = data)
    tree = html.fromstring(response.content)
    hakka = tree.xpath("/html/body/table[2]/tr[2]/td[2]/text()")
    if len(hakka) != 0:
        res = hakka[0][:-1]
        if "-" in res:
            return res[:res.index("-")]
        return res
    else:
        res = getjp(s)
        return res


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

    if byte_lst[0] == '\xef' and byte_lst[1] == '\xbb' and byte_lst[2] == '\xbf':
        len_kept = 3 - len(byte_lst) # keep all chars after the first 3 BOM
        s = ''.join(byte_lst[len_kept:])
        s = s.decode('utf-8')
    return s


def exclude_non_chinese(s):
    exclude = []
    for i in range(33, 128):
        exclude.append(chr(i))
    chinese_punc = [u'\u3000', u'\u3001', u'\u3002', u'\u3008', u'\u3009', u'\u300a', u'\u300b', u'\u300c', u'\u300d', u'\u300e', u'\u300f',
                    u'\u3010', u'\u3011', u'\u301d', u'\u301e', u'\uff01', u'\uff02', u'\uff03', u'\uff04', u'\uff05', u'\uff06', u'\uff07',
                    u'\uff08', u'\uff09', u'\uff0c', u'\uff0f', u'\uff1a', u'\uff1b', u'\uff1f', u'\uff3b', u'\uff3d']
    exclude = exclude + chinese_punc
    exclude = set(exclude)
    s = ''.join(ch for ch in s if ch not in exclude)
    return s


def romanize(chn_char, dialect):
    if dialect == 'cantonese':
        romanized = getjp(chn_char)
    if dialect == 'hakka':
        romanized = gethakka(chn_char)

    # separate tone and pronounciation
    if any(char.isdigit() for char in romanized):
        r_notone = romanized[:-1]
        tone = romanized[-1]
    else:
        r_notone = romanized
        tone = str(0)
    # generate the spaced pronounciation
    r_spaced = ""
    for char in r_notone:
        r_spaced += char
        r_spaced += " "
    r_spaced = r_spaced[:-1]

    res = []
    res.append(r_notone)
    paran = "((" + r_spaced + ") " + tone + ")"
    res.append(paran)

    return res


def get_value(word, dialect):
    pre = "(lex.add.entry \'(\"" # followed by r_notone
    mid = "\" nn (" # followed by r_spaced
    end = ")))"

    notone = ""
    secundo = ""
    for chn_char in word:
        #ord(chn_char.decode('utf-8'))
        if 19968 <= int(str(hex(ord(chn_char))), 16) <= 40959 or 13312 <= int(str(hex(ord(chn_char))), 16) <= 19903:
            roman_list = romanize(chn_char, dialect)
            notone += roman_list[0]
            secundo += roman_list[1]
            secundo += " "
    secundo = secundo[:-1]
    value = pre + notone + mid + secundo + end
    return value

def make_dict(s, dialect):
    word_list = s.split()
    word_list = set(word_list)

    print len(word_list)
    counter = 0
    res_name = dialect + "_lexicon_entries.data"
    res = codecs.open(res_name, 'w', 'utf-8')
    for word in word_list:
        print counter
        print word
        res.write(get_value(word, dialect) + '\r' + '\n')
        #res.write('\n')
        counter += 1
    res.close()


s = read_check_bom("gan_all.txt")
s = exclude_non_chinese(s)
make_dict(s, 'cantonese')
#make_dict(s, 'hakka')
