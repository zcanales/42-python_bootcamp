import numpy as np

class ScrapBooker:
        @staticmethod
        def crop(array, dimensions, position=(0, 0)):
                """
                crops the image as a rectangle with the given dimensions
                (meaning, the new height and width for the image)
                whose top left corner is given by the position argument.
                The position should be (0,0) by default. You have to consider it an error (and handle said error)
                if dimensions is larger than the current image size.
                :param array: NumPy Array
                :param dimensions:
                :param position:
                :return: NumPy Array
                """
                return (array[position[0]:dimensions[0], position[1]:dimensions[1]])
        @staticmethod
        def thin(array, n, axis):
                """
                deletes every n-th pixel row along the specified axis (0 vertical, 1 horizontal), example below.
                :param array:
                :param n:
                :param axis:
                :return:
                """
                return np.delete(array, n, axis)
        @staticmethod
        def juxtapose(array, n, axis):
                """
                juxtaposes n copies of the image along the specified axis (0 vertical, 1 horizontal).
                :param array:
                :param n:
                :param axis:
                :return:
                """
                if axis:
                        return np.tile(array, (1, n))
                else:
                        return np.tile(array, (n, 1))

        @staticmethod
        def mosaic(array, dimensions):
                """
                makes a grid with multiple copies of the array.
                The dimensions argument specifies the dimensions
                (meaning the height and width) of the grid (e.g. 2x3).
                :param array:
                :param dimensions:
                :return:
                """
                return np.tile(array, dimensions)

if __name__ == "__main__":
        a = ScrapBooker
        array = np.chararray((11, 12), unicode=True)
        i = 0
        j = 0
        while j < 11:
            while i < 12:
                array[j][i] = chr(65 + i)
                i += 1
            i = 0
            j += 1
        print(f"normal -> {array}")
        crop = a.crop(array, (3,5), (2,1))
        print(f"crop -> {crop}")
        thin = a.thin(array, n=8, axis=0)
        print(f"thin -> {thin}")
        n = a.juxtapose(array, (2), 1)
        print(f"juxtapose -> {n}")
        print(f"mosaic -> {a.mosaic(array, (2, 3))}")

      #  m = ScrapBooker.mosaic(array, (2, 2))
      #  print(f"mosaic -> {m}")
        #print(n)
