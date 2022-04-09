import os
from io import StringIO
import PIL.Image
import PIL.ImageChops


U = PIL.Image.open("Images/kiran1.jpg")
I = PIL.Image.open("Images/kiran2.jpg")
difference = PIL.ImageChops.difference(I, U)
difference.save("Images/difference.png")