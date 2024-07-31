from urllib.request import urlretrieve
from PIL import Image


image_url = "https://i.pinimg.com/736x/9c/9b/e7/9c9be78eb0e51b298f06dddf0dbd1223.jpg"

urlretrieve(image_url, "bat.jpg")

image  = Image.open("bat.jpg")
image.show()
