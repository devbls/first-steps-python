for sqrt in range(32, 100):
    num = sqrt ** 2
    lower = num % 100
    greater = num // 100

    if (lower + greater) == sqrt:
        print(num)
        print(lower)
        print(greater)
        print(sqrt)

print("Square root is: ", sqrt)