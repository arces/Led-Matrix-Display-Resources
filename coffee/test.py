import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32, 4)

while True:
        for n in range(0,3):
                image = Image.open(str(n)+".gif")
                image.load()          # Must do this before SetImage() calls
                matrix.SetImage(image.im.id)
                time.sleep(0.3)

matrix.Clear()
#matrix.Fill(0x6F85FF) # Fill screen to sky color
#while True:
#        for n in range(32, -image.size[0], -1): # Scroll R to L
#                matrix.SetImage(image.im.id, n, 0)
#                time.sleep(0.025)


