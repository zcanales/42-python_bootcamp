import functools

def ft_reduce(function_to_apply, list_of_inputs):
    if not callable(function_to_apply) or \
        not hasattr(list_of_inputs, '__iter__'):
        print("Error")
        return False
    total = list_of_inputs[0]
    for l in range(1, len(list_of_inputs)):
        total = function_to_apply(total, list_of_inputs[l])
    return total




lst = [1, 2, 10, 23]
ft_function = lambda x, y: y if x > y else x
#ft_function = lambda x, y: y + x
print(functools.reduce(ft_function, lst))
print(ft_reduce(ft_function, lst))