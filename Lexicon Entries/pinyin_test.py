import codecs
import re

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
# ( let_u_umlaut (( y: )))

def uni(num):
    return unichr(num)

def space(s):
    grapheme_mapping = {'a':'A', 'c':'ch', 'j':'dZ', 'q':'QM', 'x':'k s', unichr(252): 'y:', 'y': 'j'}
    r_spaced = ""
    for empty in (' ', '\r', '\n'):
        if empty in s:
            s = re.sub(empty, '', s)
    for char in s:
        if char in grapheme_mapping:
            r_spaced += grapheme_mapping[char]
        else:
            r_spaced += char
        r_spaced += " "
    r_spaced = r_spaced[:-1]

    return r_spaced


def get_value(pinyin):
    toned_char = []
    for i in [275, 233, 283, 232, 299, 237, 464, 236, 257, 225, 462, 224, 363, 250, 468, 249, 333, 243, 466, 242, 470, 472, 474, 476]:
        toned_char.append(uni(i))

    e = toned_char[0:4]
    i = toned_char[4:8]
    a = toned_char[8:12]
    u = toned_char[12:16]
    o = toned_char[16:20]
    v = toned_char[20:24]
    toned_char_group = [e, i, a, u, o, v]
    toned_group_name = ['e', 'i', 'a', 'u', 'o', unichr(252)]
    grapheme_mapping = {'a':'A', 'c':'ch', 'j':'dZ', 'q':'QM', 'x':'k s', unichr(252):'y:', 'y':'j'}

    char_pinyin_list = pinyin.split(' ') # each character
    line_list = []
    for char_pinyin in char_pinyin_list: # pinyin of each character
        sublist = []
        pinyin_notone = ""
        #pinyin_graphemable = "" # for spacing
        for char in char_pinyin: # each character
            if char in toned_char:
                toned_index = toned_char.index(char)
                tone = str(toned_index%4 + 1)
                sublist.append(tone)
                #if toned_index/4 == 5:
                #    pinyin_notone += unichr(252)
                #    pinyin_graphemable += unichr(252)
                #elif toned_index/4 == 2:
                #     pinyin_notone += 'a'
                #    pinyin_graphemable += 'a'
                #else:
                pinyin_notone += toned_group_name[toned_index/4]
                #pinyin_graphemable += toned_group_name[toned_index/4]
            else:
                pinyin_notone += char
                #if char not in grapheme_mapping:
                #    pinyin_notone += char
                #else:
                #    pinyin_notone += grapheme_mapping[char]

        if len(sublist) == 0:
            sublist.append('0')
        sublist.append(pinyin_notone) # for each char, with 2 elements, tone and notone
        #sublist.append(pinyin_graphemable)
        line_list.append(sublist) # for each word

    pre = "(lex.add.entry \'(\"" # followed by r_notone
    mid = "\" nn (" # followed by r_spaced
    end = ")))"
    entry = pre
    s_notone = ''

    for sublist in line_list:
        s_notone += sublist[1]
    entry = entry + s_notone + mid
    for sublist in line_list:
        paran = "((" + space(sublist[1]) + ") " + sublist[0] + ")"
        entry = entry + paran + " "
    entry = entry[:-1]
    entry += end
    return entry

def write_file(s_list):
    res_name = "mandarin" + "grapheme_lexicon_entries4.data"
    res = codecs.open(res_name, 'w', 'utf-8')
    counter = 0
    for s in s_list:
        print counter
        print s
        value = get_value(s)
        for empty in ('\r', '\n'):
            if empty in value:
                value = re.sub(empty, '', value)
        res.write(value + '\r' + '\n')
        counter += 1
    res.close()

# intersection = [char for char in pinyin if char in toned_char]
# but don't know the position of light tone
# http://stackoverflow.com/questions/11328940/check-if-list-item-contains-items-from-another-

#f = codecs.open('pinyin.word.txt', 'r', 'utf-8')
#s = f.readlines()
# No BOM in yinpin.word.data
s_check = read_check_bom('pinyin.word.txt')
s_list = s_check.split('\n')
write_file(s_list)
