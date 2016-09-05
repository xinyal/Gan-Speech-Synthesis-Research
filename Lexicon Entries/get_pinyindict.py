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

    print byte_lst[:10]
    if byte_lst[0] == '\xef' and byte_lst[1] == '\xbb' and byte_lst[2] == '\xbf':
        len_kept = 3 - len(byte_lst) # keep all chars after the first 3 BOM
        s = ''.join(byte_lst[len_kept:])
        s = s.decode('utf-16')
        return s
    s = ''.join(byte_lst)
    s = s.decode('utf-16')
    return s

def space(pinyin):
    pinyin_spaced = ""
    for char in pinyin:
        pinyin_spaced += char
        pinyin_spaced += " "
    pinyin_spaced = pinyin_spaced[:-1]
    return pinyin_spaced

def get_value(word):
    toned_char = [275, 233, 283, 232] + [299, 237, 464, 236] + [257, 225, 462, 224] + [363, 250, 468, 249] + [333, 243, 466, 242] + [470, 472, 474, 476]
    e = [275, 233, 283, 232]
    i = [299, 237, 464, 236]
    a = [257, 225, 462, 224]
    u = [363, 250, 468, 249]
    o = [333, 243, 466, 242]
    y = [470, 472, 474, 476]
    toned_char_group = [e, i, a, u, o, y]
    toned_group_name = ['e', 'i', 'a', 'u', 'o', unichr(252)]
    #unichr(252)

    wordlist = word.split()

    pre = "(lex.add.entry \'(\"" # followed by r_notone
    mid = "\" nn (" # followed by r_spaced
    end = ")))"
    s_notone = word
    tone = []
    res = ""

    word_counter = 0
    for pinyin in wordlist:
        word_counter += 1
        for char in pinyin:
        # intersection = [char for char in pinyin if char in toned_char]
        # but don't know the position of light tone
        # http://stackoverflow.com/questions/11328940/check-if-list-item-contains-items-from-another-list
            for i in range(0, len(toned_char_group)):
                if char in toned_char_group[i]:
                    s_notone = re.sub(char, toned_group_name[i], s_notone)
                    tone.append(str(toned_char_group[i].index(char) + 1))
        if len(tone) < word_counter:
            tone.append("0")

    wordlist = word.split()
    s_notone = re.sub(" ", "", s_notone)
    res = pre + s_notone + mid

    for chn_pinyin in wordlist:
        i = 0
        pinyin_spaced = space(chn_pinyin)
        res = res + "((" + pinyin_spaced + ")" + tone[i] + ")"
    res += end
    return res

def write_pinyin_value(s):
    word_list = s.split('\xff\xfe\n\x00')
    #print word_list[]
    res_name = "mandarin" + "_lexicon_entries.data"
    #res = codecs.open(res_name, 'w', 'utf-8')
    res = codecs.open(res_name, 'w', 'utf-16')
    counter = 0
    for word in word_list:
        print counter
        res.write(get_value(word))
        res.write('\r\n')
        counter += 1
    res.close()

s = read_check_bom('pinyin.word.data')
write_pinyin_value(s)
#print ' '.join(s.split()[:10]
