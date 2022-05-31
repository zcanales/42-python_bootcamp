def ft_map(function_to_apply, list_of_inputs):
    if not callable(function_to_apply):
        print("First parameter must be a funcion")
        return False
    if not hasattr(list_of_inputs, '__iter__'):
        print("Second parameter must be iterable")
        return False
    return ([function_to_apply(l) for l in list_of_inputs])
    #for l in list_of_inputs:
     #   yield (function_to_apply(l))



def ft_pwd(l):
    return l * 2

lst = range(5)
print(ft_map(ft_pwd, lst))
print(ft_map(lambda x: x - 2, lst))
print(ft_map(lambda x: x - 2, 5))
print(ft_map("hola", lst))