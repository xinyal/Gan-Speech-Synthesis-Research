#with open("test.txt", "rb") as f:
    #byte = f.read(1)
    #while byte != "":
        # Do stuff with byte.
        #byte = f.read(1)
        #print repr(byte)


#print repr(byte)

def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

# example:
#for b in bytes_from_file('test.txt'):
#    print b.encode('big5')
#    print repr(b)

msg = u'šâ'
encoded = msg.encode('big5')
print encoded
