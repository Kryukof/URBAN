def print_params(a = 1, b = "string", c = True):
    print(a, b, c)



values_list = [False, "4, 5, 6", 7]
values_dict = {"a": 7, "b": True, "c": "raketa"}
values_list_2 = [54.32, "Stroka"]
print_params(*values_list_2, 42)
print_params(*values_list)
print_params(**values_dict)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])



