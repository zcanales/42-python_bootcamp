if __name__ == '__main__':
    from vector import Vector
try:
    v1 = Vector([1, 13.0, -2, 3.0])
    print(v1)
    v2 = Vector([50, 3.0, 4, 2.0])
    v5 = v1 / v2
    print(v5)
    print()

except (Exception, ValueError) as e:
    print("FIn: ", repr(e))
