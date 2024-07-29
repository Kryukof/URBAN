def print_params(a, b, c):
     print(a, b, c)

values_list = [False, "4, 5, 6", 7]
values_dict = {"a": 7, "b": True, "c": "raketa"}
values_list_2 = [54.32, "'Stroka'"]
print_params(*values_list_2, 42)

