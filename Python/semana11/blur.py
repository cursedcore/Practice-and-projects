from PIL import Image, ImageFilter, ImageOps

before = Image.open("porsche.jpg")
after = before.filter(ImageFilter.BoxBlur(10))
mirrorr = ImageOps.mirror(before)

mirrorr.save('reflectBlur.jpg')
after.save("blurryblur.jpg")
#grayscalee.save("grayBlur.jpg")