import re
import codecs


# To clear the huge amount of repeated sentences
# containing ascii characters (0-9a-zA-Z)
# containing the pattern of "help" in traditional chinese
# and containing the pattern of "category" in traditional chinese



text = ''.join(codecs.open('wiki4copy.txt', 'r', 'utf-8'))
text = re.split('\n', text)

# open the file
output = codecs.open('wiki4clear2.txt', 'w', 'utf-8')


pattern = []
pattern += ['.*\w+'] # clear all non-Chinese characters (0-9a-zA-Z_)
                     # pattern: match any sentence that contains \w
pattern += [ur'[\u5e6b]'ur'[\u52a9] : ']  # "help"
pattern += [ur'[\u5206]'ur'[\u985e] : ']  # "category"

pattern = "|".join(pattern)
for line in text:
    if not re.search(pattern,line):
        s = line + "\n"
        output.write(s)
        #chinesetext += line + "\n"
        #chinesetext += '\n'

output.close()
#print chinesetext
    
        
    
#pattern = []
