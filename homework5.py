immutable_var = (1, 2, 3, "a", "b", True, False, 0.125)
print(immutable_var)

#immutable_var[0] = [200]  Является неизменяемым обьектом

mutable_list = [[1, 2, 3], "a", "b"]
mutable_list[0][1] = 0
print(mutable_list)
