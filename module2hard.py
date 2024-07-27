number = int(input("Enter the number: "))
list_ = []
for i in range(1, number + 1):
    for j in range(1, number + 1):
        if number % (i + j) == 0 and i < j:
            list_.append(i)
            list_.append(j)
print(*list_, sep="")
