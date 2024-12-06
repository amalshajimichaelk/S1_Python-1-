def fibonacci_series(n):
    a,b=0,1
    fibonacci = []
    while a <= n:
        fibonacci.append(a)
        a,b=b,a+b
    return fibonacci
