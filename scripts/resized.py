from PIL import Image
import os

path = '/home/darshan/Documents/anyproimage/Alcho_025/Bardog/'
scale = 0.25  # Aspect ratio wrt original size

def resize():
    dirs = os.listdir(path)
    for item in dirs:
        if item == '.jpeg':
            continue
        if os.path.isfile(path+item):
            image = Image.open(path+item)
            file_path, extension = os.path.splitext(path+item)
            target_path = '/home/darshan/Documents/anyproimage/Alcho_025/Bardog_resized/'
            height = int(image.size[0] * scale)
            width = int(image.size[1] * scale)
            image = image.resize((height, width), Image.Resampling.LANCZOS)
            image.save(target_path + "_scale" + extension, 'JPEG', quality=100)

resize()