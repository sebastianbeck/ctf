from PIL import Image
from PIL import ImageDraw
from PIL import ImageEnhance
     
img = Image.new('L', (500, 500))
draw = ImageDraw.Draw(img)
draw.rectangle(((0, 00), (500, 500)), fill="white")
draw.rectangle(((250, 10), (255, 14)), fill="black")
pix = img.load()
x=50
y=10
while y < 200:
    while x < 450:
        #algo
        pix = img.load()
        #if(pix[x,y-5] == 0):
        if((pix[x-5,y-5] == 0) != (pix[x,y-5] == 0 or pix[x+5,y-5] == 0)):
            draw.rectangle(((x, y), (x+5, y+5)), fill="black")
            print(x,y)
    #[left_cell XOR (central_cell OR right_cell)] 
        x=x+5
    y=y+5
    x=0
img.save('file.png')


