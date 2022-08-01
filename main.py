import os
import json
from PIL import Image
from PIL.ExifTags import TAGS


    
# Get the list of all files and directories
path = "input"
files = os.listdir(path)
 
id_file = open("last_id.txt", "r+")
id = int(id_file.readline())

path = "photos"
donefiles = os.listdir(path)

if(len(donefiles) == 0):
    id = 0
    
if len(files) > 1:
    for file in files:
        id+=1 
        foo = Image.open('input/'+file)
        if foo.size[0] > 2000 or foo.size[1] > 2000:
            opt_w = int(foo.size[0]) * 0.3
            opt_h = int(foo.size[1]) * 0.3
            print(opt_w,opt_h)            
            foo = foo.resize((int(opt_w),int(opt_h)) ,Image.ANTIALIAS)
        foo.save('photos/'+str(id).zfill(3)+'.jpg',optimize=True,quality=95)
        #os.rename('input/'+file, 'photos/'+str(id).zfill(3)+'.jpg')            
        id_file.seek(0)
        id_file.write(str(id))
        id_file.truncate() 

    print("files renamed successfully")
else:
    print("there are no photos")
