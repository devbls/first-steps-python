def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = eval(input("Type an integer number: "))
print(f"The factorial of {number} is {factorial(number)}")