import codecs


# Firstly, read the file in bytes and
# append them to a list, 
# to remove the BOM (whatever before the \n). 
f = open('test.txt', 'rb')
byte_lst = []
try:
    byte = f.read(1)
    while byte != '':
        # print byte
        byte_lst.append(byte)
        byte = f.read(1)
finally:
    f.close()              # Reading and appending finished
                           # byte_lst is the list


# Then decode the string in utf-8 and encode it in big5
# (python seems not to be able to decode a string in big5,
#  see https://www.ptt.cc/bbs/Python/M.1380034106.A.553.html)

s = ''.join(byte_lst[-3:]) # ['\xef', '\xbb', '\xbf', '\r', '\n', '\xe9', '\x9b', '\x85']
                     # The last 3 bytes are the character
                     # Join them to a string to decode in utf-8 soon. 

print repr(s)        # in unicode

#utf = repr(s.decode('utf-8')) # this is the utf-8 code of the character.
                              # Just for reference, to make sure that
                              # python decodes the character to the right
                              # utf-8 code (without garbling it).
                              # so that the utf-8 code to big5 convertion would
                              # be successful

                              # check it with the utf-8 table online
                              # see if the output matches the utf-8 code of the char
big5code = repr(s.decode('utf-8').encode('big5'))
print repr(s.decode('utf-8').encode('big5'))

