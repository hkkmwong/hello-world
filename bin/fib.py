def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
i = 1
while i < 50:
    print(i, fib(i))
    i += 1
print('end')
