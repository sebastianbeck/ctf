import numpy as np
import matplotlib.pyplot as plt

def create_rule30_pattern(display=True):
        
    #Create np array as empty canvas
    canvas = np.zeros((50,100))
    canvas = canvas.astype(int)

    #Set starting Pixel
    canvas[0, 50] = 1

    #Rule 30 algorithm, see: https://en.wikipedia.org/wiki/Rule_30#Rule_set
    for row in range(1, np.shape(canvas)[0]):
        for col in range(1, np.shape(canvas)[1] - 1):
            canvas[row, col] = canvas[row-1, col - 1] ^ (canvas[row-1, col] | canvas[row-1, col + 1])

    #Invert image
    canvas = canvas ^ 1

    if display:
        _, ax = plt.subplots(1,1,figsize=(20,20))
        ax.imshow(canvas,cmap='gray')
        ax.title.set_text('rule 30')
        ax.axis('off')
        plt.show()

    return canvas
create_rule30_pattern()