import os
opn3 = open("directory.txt","r")
path= opn3.read()
print(path)
path2 = isinstance(path , str)
print(path2)
opn3.close()