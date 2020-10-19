from PIL import Image

im = Image.open('qr.png') # Can be many different formats.
pix = im.load()
#print (im.size)  # Get the width and hight of the image for iterating over
x=1
y=1
width, height = im.size
while y < height:
    while x < width:
        #corner exception
        if((x < 40 and y < 40) or (x > 125 and y <40) or (x<40 and y > 125)):
            print("X ", end="")
        else:
            #255 white and 0 is black
            if pix[x,y] == 0:
                print("0 ", end="")
            else:
                print("1 ", end="")
            #xor with the rule 30
        x=x+5
    x=1
    print("")
    y=y+5
#1 dot is 5x5 pix we need to get the colors in an list 40 40  oben rechts und links 
#print (pix[x,y])  # Get the RGBA Value of the a pixel of an image
#ix[x,y] = value  # Set the RGBA Value of the image (tuple)
#im.save('qr.jpg')  # Save the modified pixels as .png