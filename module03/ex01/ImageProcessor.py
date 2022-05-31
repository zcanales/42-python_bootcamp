from matplotlib import image
from matplotlib import pyplot
import numpy as np
from PIL import Image


class ImageProcessor():
    @staticmethod
    def load(path):
        try:
            loaded_img = image.imread(path)
        except:
            exit("not good path")
        print("Loading a img of {} * {} dimension".format(loaded_img.shape[0], loaded_img.shape[1]))
        return loaded_img
    @staticmethod
    def display(array):
        imgplot = pyplot.imshow(array, interpolation="nearest")
        imgplot.set_cmap('nipy_spectral')
        pyplot.colorbar()
        pyplot.show()

"""class ImageProcessor:
    @staticmethod
    def load(path):
        # load image as pixel array
        img = image.imread(path)

        # convert image to numpy array
        array = np.asarray(img)
        array = (array * 255).astype("uint8")
        print("Loading image of dimensions {} * {}".format(img.shape[0], img.shape[1]))
        return array

    @staticmethod
    def display(array):
        # draw image
        pyplot.imshow(array, interpolation='nearest')
        # show image
        pyplot.show()
        return"""

if __name__ == "__main__":
    a = ImageProcessor()
    array = a.load("422.png")
    a.display(array)
