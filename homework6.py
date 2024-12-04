my_dict = ({"Igor": 1984, "Tanja": 1955})
print(my_dict)
print(my_dict["Igor"])
print(my_dict.get("Natasha"))
#print(my_dict.update({"Egor": 1997, "Sara": 2000})) Почему такой вариант не работает?
my_dict.update({"Egor": 1997, "Sara": 2000})
print(my_dict)
delete = my_dict.pop("Sara")
print(delete)
print(my_dict)


my_set = {1, 2, 3, 3, 8, 3, 2, 1, 3, 2, 8}
print(set(my_set))
my_set.add(5)
my_set.add(4)
print(my_set)
my_set.discard(8)
print(my_set)