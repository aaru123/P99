import os
import shutil

path = "/Users/aryanagrwal/Documents/whitehat/python/C99"
list = os.lisdir(path)
for i in list: 
    name, ext = os.path.splitext(i)
    # stores the ext 
    
    ext = ext[1:]
    
    if ext == '':
        continue
    # start from here