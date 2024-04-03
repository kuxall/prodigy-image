# import os
from PIL import Image

# # directory containing the images
# img_dir = "/home/darshan/Documents/anyproimage/Alcho_025/Avion"

# # desired size for the images
# resize_to = (640, 480)

# # loop through all files in the directory
# for filename in os.listdir(img_dir):
#     # check if the file is an image
#     if not filename.endswith(".jpeg") and not filename.endswith(".png"):
#         continue

#     # open the image
#     img = Image.open(os.path.join(img_dir, filename))
#     # resize the image
#     img_resized = img.resize(resize_to)
#     # save the resized image
#     img_resized.save(os.path.join(img_dir, "resized_" + filename))


import os

# specify the folder where the original images are stored
input_folder = "/home/darshan/Documents/anyproimage/Alcho_025/Avion/"
# specify the folder where the resized images will be stored
output_folder = "/home/darshan/Documents/anyproimage/Alcho_025/Avion_resize"
# specify the desired scaling factor
scaling_factor = 0.5
# loop through all files in the input folder
for filename in os.listdir(input_folder):
    # open the image file
    with Image.open(os.path.join(input_folder, filename)) as img:
        # get the original height and width of the image
        original_width, original_height = img.size
        # calculate the new height and width by multiplying by the scaling factor
        width = int(original_width * scaling_factor)
        height = int(original_height * scaling_factor)
        # resize the image
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        # save the resized image to the output folder
        img.save(os.path.join(output_folder, filename))