a, b = 0, 1

fib = [a]

for x in range(5):
    a, b = b, a + b
    fib.append(a)

print(fib)