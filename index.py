from PIL import Image

def thumbnail(img_name, img_save):
  image = Image.open(img_name)
  image.thumbnail((512,512))
  image.save(img_save)

def resize(img_name, img_save):
  image = Image.open(img_name)
  new_image = image.resize((512,512))
  new_image.save(img_save)

resize('Academia Campestre.png', '20304_logo1.png')