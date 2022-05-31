def ft_filter(function_to_apply, list_of_inputs):
    if not callable(function_to_apply) or \
        not hasattr(list_of_inputs, '__iter__'):
        print("Error")
        return False
    ret = []
   # ret.append([l for l in list_of_inputs if function_to_apply(l)])
   # return ret
    for elem in [l for l in list_of_inputs if function_to_apply(l)]:
        yield elem

lst = [1, 2,3 ,4,  5, 6 ,7]
print(ft_filter(lambda x : (x % 2 == 0), lst))
print(list(ft_filter(lambda x : (x % 2 == 0), lst)))
#print(list(filter(lambda x : (x % 2 == 0), lst)))