def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

print(fibonacci(10))

0 1 1 2 3 5 8 13 21 34 55
