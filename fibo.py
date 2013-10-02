def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a
    

#print fibonacci(1000)


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(5) == 5
