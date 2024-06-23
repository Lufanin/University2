def print_params(a = 1, b = 'Строка', c = True):
    print(a,b,c)


values_list=[False, 'Hello', 54]
values_dict={'a': None, 'b': "way", 'c': 99 }
values_list2=[54.32, 'Строка']
print_params(b = 25)
print_params(c = [1,2,3])
print_params(b = 25,c = [1,2,3])
print()
print_params(*values_list)
print_params(**values_dict)
print()
print_params(*values_list2, 42)

