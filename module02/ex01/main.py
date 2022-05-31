def what_are_the_vars(*args, **kwarg):
    obj = ObjectC()

    for key, value in kwarg.items():
       # print("kwarg == {} -> {}".format(key, value))
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)
            
    i = 0
    for a in args:
      #  print("args == {}".format(a))
        s = "var_" + str(i) 
        if hasattr(obj, s):
            return None
        setattr(obj, s, a)
        i += 1
    return obj

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return 
    for attr in dir (obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a = 10, hello = "word")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="word")
    doom_printer(obj)

