from PIL import Image
import os

def thumbnail(img_name, img_save, height = 1024, width= 1024):
  if os.path.isfile(img_name):
    image = Image.open(img_name)
    image.thumbnail((height, width))
    image.save(img_save)
    print('Logo criada')
  else:
    print('Imagem não encontrada')

def resize(img_name, img_save, height = 1024, width= 1024):
  if os.path.isfile(img_name):
    image = Image.open(img_name)
    new_image = image.resize((height, width))
    new_image.save(img_save)
    print('Logo criada')
  else:
    print('Imagem não encontrada')

resize('Endurance.jpg', '21621_logo1.png')