# Output all Fibonacci Numbers up to or lower than the maximum number input

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end = "  ")
		a, b = b, a+b
	print()

inp = int(input("Enter max number: "))
fib(inp)
