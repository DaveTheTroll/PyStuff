import os
import cv2
from matplotlib import pyplot as plt

def processFolder(src, fType, dest):
    for f in os.listdir(src):
        if f.endswith("."+fType):
            name = os.path.join(src, f)
            print(name)
            img = cv2.imread(name, 0)
            plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
            plt.xticks([]), plt.yticks([])
            plt.show()

if __name__ == "__main__":
    processFolder("C:\\Users\\dave\\Dropbox\\RP\\Vor'Azi", "png", "D:\\Temp\\Maps")