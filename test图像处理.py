from PIL import Image

im = Image.open("1.png")
print(im.format,im.size,im.mode) 

box = (50,100,718,924)
region = im.crop(box)


region.show()
region.save("4.jpg")
