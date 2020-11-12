from PIL import Image
import numpy
import random

x,y = 100,100
value = 255,0,0
listStep = []
filein = input("Please Enter an Image File (with extension): ")
fileout = input("Please Enter a Name For Your New Image (with extension): ")
if(fileout == ""):
    fileout = "processed_"+filein

im = Image.open(filein) # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
for i in range(im.size[0]):
    for j in range(im.size[1]):
        listStep = list(pix[i,j])  # Get the RGBA Value of the a pixel of an image
        listStep = [int(x+(255-x)*numpy.sin(x)) for x in listStep]
        #listStep[3] = 255
        pix[i,j] = tuple(listStep) # Set the RGBA Value of the image (tuple)
im.save(fileout)  # Save the modified pixels as .png