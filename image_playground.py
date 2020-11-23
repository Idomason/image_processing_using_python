
# The AIM of this project is convert image file extensions
# from .jpg to .png and also change images using PIL module.

# Import sys, os and PIL module

import sys
import os
from PIL import Image, 

# Grab the image folder and processed_image folder using sys module
image_folder = sys.argv[1]
processed_image = sys.argv[2]

# create processed_image folder if not found in the dir
if not os.path.exists(processed_image):
    os.makedirs(processed_image)

# Change the extension of the image files in the the image_folder from
# .jgp to .png and then finally store them in a new folder called New.
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{processed_image}{clean_name}.png', 'png')
    print('All done!')
