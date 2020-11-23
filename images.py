# The aim of this project is to convert image colors,
# blur images, resize image and rotate images using the PIL module

# Import Image and ImageFilter from PIL
from PIL import Image, ImageFilter

# Blur the image file (pikachu.jpg) in the Images folder and rename it
# to blur.png
filename = './Image Processing/Images/pikachu.jpg'
img = Image.open(filename)
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')
filtered_img.show()


# Covert the image file from the original color to grey color
# and rename it to grey.png
img = Image.open(filename)
converted_img = img.convert('L')
converted_img.save('grey.png', 'png')
converted_img.show()


# A Resized image
filename = './Image Processing/Images/pikachu.jpg'
img = Image.open(filename)
converted_img = img.resize((300, 300))
converted_img.save('newSize.png', 'png')
converted_img.show()

# Rotate the image file
img = Image.open(filename)
crooked = img.rotate(180)
crooked.save('crooked.png', 'png')
crooked.show()

