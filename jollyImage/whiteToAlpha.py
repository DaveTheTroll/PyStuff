import os
from matplotlib import pyplot as plt
import sys
import numpy as np

def processFolder(src, fType, dest):
    for f in os.listdir(src):
        if f.endswith("."+fType):
            name = os.path.join(src, f)
            print(name)
            img = plt.imread(name)
			
            alpha = np.zeros((img.shape[0], img.shape[1], 4))
            img2 = np.square(img)
            alpha[:,:,3] = 1-np.sqrt(np.mean(img2, axis=2))
            
            plt.subplot(211)
            plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
            plt.xticks([]), plt.yticks([])
            
            plt.subplot(212)
            plt.imshow(alpha, cmap = 'gray', interpolation = 'bicubic')
            plt.xticks([]), plt.yticks([])
            plt.show()
            
            name = os.path.join(dest, f)
            print(name)
            print(alpha)
            print(img.shape)
            plt.imsave(name, alpha)
			
if __name__ == "__main__":
	if len(sys.argv) > 2:
		processFolder(sys.argv[1], "png", sys.argv[2])
	else:
		print("Arguments required: SRC FOLDER, DEST FOLDER")