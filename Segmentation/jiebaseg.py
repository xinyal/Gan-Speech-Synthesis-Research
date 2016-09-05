# encoding=utf-8
import jieba
import codecs


jieba.set_dictionary('jieba\dict.txt.big')
#jieba.set_dictionary('dict.txt.big')
jieba.load_userdict("jieba\gandictonly.txt")
#jieba.load_userdict("jieba\dict.txt")

text = ''.join(codecs.open('wiki_05_sent', 'r', 'utf-8'))
seg_list = jieba.cut(text, cut_all=False)
# cut_all = True: full mode
# cut_all = False: precise mode
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

res = r"/ ".join(seg_list)
print type(res)
print len(res)
#output = codecs.open('jiebafull', 'w', 'utf-8')
output = open('jiebafull', 'w')
output.write(" ".join(seg_list))
output.close()
    

