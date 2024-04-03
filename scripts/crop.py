from PIL import Image
import os.path, sys
path = '/home/darshan/Pictures/download images/annotation Images/reposado_big_corralejo/'
dirs = os.listdir(path)
# all the pixels are measured from left top corner of the photor
# must be an integer values
x1=200
x2=880
y1=0.5
y2=1900
# Function to crop the image
def crop():
    for item in dirs:
        absolutepath = os.path.join(path,item)
        if os.path.isfile(absolutepath):
            img = Image.open(absolutepath)
            # f = "/home/darshan/Documents/anyproimage/Alcho_025Cropp/"
            f, e = os.path.splitext(absolutepath)
            croppedImg = img.crop((x1, y1, x2, y2))
            croppedImg.save(f + '_croppys.jpeg', "JPEG", quality=100)
# actual crop is performed here
crop()