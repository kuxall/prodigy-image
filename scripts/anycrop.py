from PIL import Image
import os.path, sys
# Path of image folder (one folder at a time, should contain only the
# images of same extension
# Absolute path is highly preferred
input_path = '/home/darshan/Documents/anyproimage/Alcho_025/Avion_resize'
# specify the folder where the cropped images will be stored
output_path = '/home/darshan/Documents/anyproimage/Alcho_025Cropp/Avion_cropped/'
# Create output folder if it does not exist
if not os.path.exists(output_path):
    os.makedirs(output_path)
dirs = os.listdir(input_path)
# all the pixels are measured from left top corner of the photo
# must be an integer values
x1=50
x2=370
y1=60
y2=920
# Function to crop the image
def crop():
    for item in dirs:
        absolutepath = os.path.join(input_path,item)
        if os.path.isfile(absolutepath):
            img = Image.open(absolutepath)
            f, e = os.path.splitext(item)
            croppedImg = img.crop((x1, y1, x2, y2))
            croppedImg.save(os.path.join(output_path, f + '_cropped.jpeg'), "JPEG", quality=100)
# actual crop is performed here
crop()