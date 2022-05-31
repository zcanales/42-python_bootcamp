class Vector:
    def __init__(self, values):
        if not isinstance(values, (int, list, tuple)):
            raise ValueError ("Values must be [int], [list] or [tuple]")
        if isinstance (values, int) and values < 0:
            raise ValueError ("Size of range cannot be negative")
        if isinstance(values, int):
            self.values = [float(nb) for nb in range(0, values, 1)]
            self.size = values
        elif isinstance(values, tuple) and len(values) == 2:
            self.values = [float(nb) for nb in range(values[0], values[1], 1)]
            self.size = values[1] - values[0]
        elif isinstance(values, list):
            self.values = values.copy()
            self.size = len(values)
    def __str__(self):
        return "{}".format(self.values)
    def __repr__(self):
        txt = str(self.values) + " : " + str(self.shape)
        return 
    def __add__(self, other_vector): 
        if not isinstance(other_vector, Vector):
            raise ValueError ("Invalid argument to add must be Vector")
        ret = []
        if other_vector.size == self.size:
            ret += ([self.values[i] + other_vector.values[i]  for i in range(self.size) ])
            return (ret)
        
    def __sub__(self, other):
       
        if not isinstance(other, Vector) or other.size != self.size:
            raise ValueError ("Invalid argument to add must be Vector and with the same size")
        ret = []
        ret += ([self.values[i] - other.values[i] for i in range(self.size)])
        return ret

    def __rsub__(self, other):
        print("Sub calle")
        return (other.sub(self))

    def __truediv__(self, other):
        if not isinstance(other, int) or other == 0:
            raise ValueError ("Invalid argument DIV > 0")
        return [self.values[i] / other for i in range(self.size)]
    def __mul__(self, other):
        if not isinstance(other, Vector) or other.size != self.size:
            raise ValueError ("Invalid argument to add must be Vector and with the same size")
        ret = []
        for i in range(self.size):
            if other.values[i] == 0:
                raise ValueError("Imposible division 0")
            ret += [self.values[i] * other.values[i]]
        return (ret)
    def __rmul__(self, other):
        if not isinstance(other, Vector) or other.size != self.size:
            raise ValueError ("Invalid argument to add must be Vector and with the same size")
        ret = []
        for i in range(self.size):
            if self.values[i] == 0:
                raise ValueError("Imposible division 0")
            ret += [self.values[i] * other.values[i]]
        return (ret)
        

        
"""        
try:
    v = Vector([1.0, 1.0, 2.5, 3.4])
    w = Vector((0, 4))
    print("Beginning")
    print(str(v))
    print(str(w))
    print("Suma")
    print(w.add(v))
    print("Resta")
 #   print(str(v))
#    print(str(w))
  #  print(w.sub(v))
 #   print(w.rsub(v))
  #'  print(v.sub(w))
    print(f"Size {v.size}")
    print(v.truediv(2))
    print(v.mul(w))

    
except (Exception , ValueError) as e:
    print("ERROR: ", repr(e))

"""