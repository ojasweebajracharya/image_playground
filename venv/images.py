# Experimenting with Pillow
from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

# You can get info about the image:
# print(img.format)
# print(img.size)
# print(img.mode)

# Add filters to the image:
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save("blur.png", "png")

# Change rotation:
# filtered_img = img.convert("L")
# crooked = filtered_img.rotate(90)
# crooked.save("grey.png","png")

# Change size:
# filtered_img = img.convert("L")
# resize = filtered_img.resize((300,300))
# resize.save("grey.png","png")

filtered_img = img.convert("L")
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png","png")

# filtered_img.show()
