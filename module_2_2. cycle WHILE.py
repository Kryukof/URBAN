first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
