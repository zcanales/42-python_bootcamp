import numpy as np
from matplotlib import image
from matplotlib import pyplot
from ImageProcessor import ImageProcessor
from PIL import Image
import PIL.ImageOps
class ColorFilter:
    @staticmethod
    def invert(array):
        """
        Takes a NumPy array of an image as an argument and returns an array with inverted color.
        Authorized functions: None
        Authorized operator: -
        """
        #Invertir la posicion
       # new_array = []
       # for i in range(len(array) - 1, 0, -1):
       #     new_array.append(array[i])
        #new_array = []
        #for i in range(3, len(array[0][0])):
        #    new_array[:,:, i] = array[:, :, i]
        new_array = array[:, :, 1]
        return 1 - array[:, :, :]
    @staticmethod        
    def to_blue(array):
        sh = array.shape
        new = np.zeros(sh)
        new[:, :, 0] = 0 #0: removing red
        new[:, :, 1] = 0 #1: removing green
        new[:, :, 2] = array[:, :, 2]
        return new
    @staticmethod        
    def to_green(array):
        new = array.copy()
        new *= [0, 1, 0]
        """ new =[201][201][4]
            for i in range(len(array)):
            j = 0
            for j in range(len(array[0])):
            k = 0
            for k in range(len(array[0][0])):
            new[i][j][k] = array[i][j][k]"""
       # new[:,:,0] *= 0
        #new[:,:,2] *= 0
        return new
    @staticmethod
    def to_red(array):
  #      new = array - ColorFilter.to_blue(array) - ColorFilter.to_green(array)
   #     return new
        blue = ColorFilter.to_blue(array)
        green = ColorFilter.to_green(array)
        red = array.copy()
        red[:,:,2] -= blue[:,:,2]
        red[:,:,1] -= green[:,:,1]
        return red
    @staticmethod
    def celluloid(array):
     #   new = array.copy()
        new = np.array(array)
        threshold = np.linspace(0, 1, num=4)
        for i in threshold:
            new[array >= i] = i
        return new
  

        

if __name__ == "__main__":
    imp = ImageProcessor()
    array = imp.load("42.png")
    clf = ColorFilter()
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[arr % 2 == 1] = -1
    print(arr)
   # array = clf.invert(array)
    #array = clf.to_blue(array)
   # array = clf.to_green(array)
   # array = clf.to_red(array)
   # array = clf.celluloid(array)
    imp.display(array)
