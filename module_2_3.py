my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while len(my_list) > count:
    if my_list[count] >= 0:
        print(my_list[count])
        count += 1
        continue
    else:
        print(f"Нашел отрицательное число: {my_list[count]}")
        break











