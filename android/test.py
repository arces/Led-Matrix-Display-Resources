#import Image
import ImageDraw
import time
from PIL import Image
#from rgbmatrix import Adafruit_RGBmatrix
from rgbmatrix import RGBMatrix, RGBMatrixOptions
#matrix = Adafruit_RGBmatrix(32, 2)

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 4
options.parallel = 1
matrix = RGBMatrix(options = options)

while True:
        for n in range(0,11):
                image = Image.open(str(n)+".gif")
                image.load()          # Must do this before SetImage() calls
                #matrix.SetImage(image.im.id)
                matrix.SetImage(image.convert('RGB'))
                time.sleep(0.08)

matrix.Clear()
#matrix.Fill(0x6F85FF) # Fill screen to sky color
#while True:
#        for n in range(32, -image.size[0], -1): # Scroll R to L
#                matrix.SetImage(image.im.id, n, 0)
#                time.sleep(0.025)


