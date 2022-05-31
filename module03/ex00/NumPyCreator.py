import numpy as np
#import random
from numpy import random
class NumPyCreator:
    def from_list(self, lst, dtype=None):
        if not isinstance(lst, list):
            return (print("Not instatiable"))
        return (np.asarray(lst, dtype))
    def from_tuple(self, lst, dtype = None):
        if not isinstance(lst, tuple):
            return (print("Not instatiable"))
        return (np.asarray(lst, dtype))
    def from_iterable(self, itr, dtype = None):
        try: 
            iter(itr)
        except:
            exit("not iterable")
        return (np.array(itr, dtype))

    def from_shape(self, shape, value=0):
        if not isinstance(shape, tuple):
            return (print("Not tuple for shape"))
        return (np.full(shape, value))
    def random(self, shape):
        return (np.random.random(shape))
    def identity(self, n):
        if not isinstance(n ,int):
            return (print("Not int in identity"))
        return (np.identity(n))

if __name__ == "__main__":
    a = NumPyCreator()
    lst = [1, 2, 3, 4, 6]
    tpl = ("a", "b", "c")
    itr = range(5)
    print(f"list -> {a.from_list(lst)}")
    print(f"tuple -> {a.from_tuple(tpl)}")
    print(f"iter -> {a.from_iterable(itr, float)}")
    print(f"shape -> {a.from_shape((4, 3), 9)}")
    print(f"random -> {a.random((4, 3))}")
    print(f"identity -> {a.identity(4)}")
    