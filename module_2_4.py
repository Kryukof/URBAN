numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
dig = 1
for i in numbers:
    for j in range(2, i - 1):
        if i % j == 0:
            not_primes.append(i)
            break

for q in numbers:
    if q not in not_primes and q != 1:
        primes.append(q)
print(primes)
print(not_primes)



