import os
import json
from PIL import Image
from PIL.ExifTags import TAGS
from decimal import *
# Get the list of all files and directories
path = "photos"
files = os.listdir(path)


def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = str(val)

    return labeled
def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()


data = []
for file in files:  
    dataIm = {}
    exif = get_exif(path+"/"+file)
    labeled = get_labeled_exif(exif) 
    img = Image.open(path+"/"+file)     
    wid, hgt = img.size

    dataIm["ID"] = os.path.splitext(file)[0] 
    dataIm["src"] = "/photos/"+os.path.splitext(file)[0]+".jpg" 
    dataIm["width"] = str(wid)
    dataIm["height"] = str(hgt)
    dataIm["ID"] = os.path.splitext(file)[0] 
    dataIm["CameraModel"] = str(labeled['Model'])
    dataIm["LensModel"] = str(labeled['LensModel'])
    dataIm["DateTime"] = str(labeled['DateTime'])
    dataIm["ISO"] = str(labeled['ISOSpeedRatings'])
    
    ratio = Decimal(str(labeled['ExposureTime'])).as_integer_ratio()

    if ratio[0] > 10:
        dataIm["ExposureTime"] = str(round(float(labeled['ExposureTime']),2))
    else:        
        dataIm["ExposureTime"] = str(ratio[0]) + "/" + str(ratio[1]) 
    dataIm["FNumber"] = str(labeled['FNumber'])
    dataIm["FocalLength"] = "f/"+str(labeled['FocalLength'])
    dataIm["Software"] = str(labeled['Software'])   
    data.append(dataIm)

jsonString = json.dumps(data, indent=4)
print(jsonString)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()