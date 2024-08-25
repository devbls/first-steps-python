def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = eval(input("Type an integer number: "))
print("Fibonacci sequence number: ", fibonacci(number))