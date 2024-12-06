import fibonaacci_numbers

n = int(input("Enter the fibonacci limit: "))
result = fibonaacci_numbers.fibonacci_series(n)
print(f"Fibonacci series upto {n}: {result}")