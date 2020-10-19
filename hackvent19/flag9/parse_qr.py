import matplotlib.pyplot as plt
import numpy as np

class QR:
    def __init__(self, path=None, remove_frame = True):
        self.img = None
        self.code = None
        self.size = None
        
        if path is not None:
            self.load(path)
            
            if remove_frame:
                self.remove_frame()
                
            self.__unscale()       
    
    def load(self, path):
        self.img = plt.imread(path)
        if self.img.ndim > 2:
            self.img = np.mean(self.img,axis=2)
            self.img = self.img.astype(int)
            
    def remove_frame(self):
        empty_lines = []
        for row in range(np.shape(self.img)[0]):
            empty = True
            for px in self.img[row, :]:
                if px == 0:
                    empty = False
                    break
                
            if empty:
                empty_lines.append(row)
                
        self.img = np.delete(self.img, empty_lines, 0)
        
        empty_lines = []
        for col in range(np.shape(self.img)[1]):
            empty = True
            for px in self.img[:, col]:
                if px == 0:
                    empty = False
                    break
            
            if empty:
                empty_lines.append(col)
                
        self.img = np.delete(self.img, empty_lines, 1)
        
    def __unscale(self):
        px_per_bit, self.size = self.__get_scaling()
        print("px_per_bit={}".format(px_per_bit))
        self.code = np.empty((self.size, self.size))
        
        for n in range(self.size):
            for m in range(self.size):
                self.code[n, m] = self.img[int(n*px_per_bit), int(m*px_per_bit)]
                self.code = self.code.astype(int)
        
    def __get_scaling(self):
        length = np.shape(self.img)[0]
        if not length%21: return length/21, 21
        elif not length%25: return length/25, 25
        elif not length%29: return length/29, 29
        elif not length%33: return length/33, 33
        
    @property
    def bits(self):
        return np.reshape(self.code ^ 1, (self.size, self.size))
            
    
qr = QR("qr.png")    
print(qr.bits)    
plt.imsave("py_qr_code.png", qr.code)


# Display the result
fig, ax = plt.subplots(3,1,figsize=(20,20))
ax[0].imshow(qr.img,cmap='gray')
ax[0].title.set_text('qr.img')
ax[1].imshow(qr.code,cmap='gray')
ax[1].title.set_text('qr.code')
ax[2].imshow(pattern_code,cmap='gray')
ax[2].title.set_text('pattern')
