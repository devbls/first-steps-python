start = int(1000**0.5) # Aproximação da raiz quadrada de 1000

if start * start < 1000:
    start += 1 # Ajusta para garantir que o quadrado seja pelo menos 1000

end = int(9999**0.5) # Aproximação da raiz quadrada de 9999

for sqrt in range(start, end + 1):
    num = sqrt ** 2
    lower = num % 100
    greater = num // 100

    if (lower + greater) == sqrt:
        print(num)
        print(lower)
        print(greater)
        print(sqrt)

print("Square root is: ", sqrt)