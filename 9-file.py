fo = open("text.txt", "wb")
fo.write("Python is a great language.\nYeah its great!!\n")
fo.close()

fo = open("text.txt", "r")
str = fo.read(10)
print "read string is: ", str

position = fo.tell()
print "current file position: ", position

position = fo.seek(0, 0)
str = fo.read(10)
print "again read string is: ", str

fo.close()

print "\n---END---\n"