def validate_cpf(cpf):
    # Remove non numeric digits
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verify if it has 11 digits
    if len(cpf) != 11:
        return False

    # Verify if all digits are equal
    if cpf == cpf[0] * 11:
        return False

    # Calculating the first verifying digit
    digitsSum = sum(int(cpf[i]) * (10 - i) for i in range(9))
    remainder = digitsSum % 11

    if remainder < 2:
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = 11 - remainder

    # Checking the first verifying digit
    if int(cpf[9]) != firstVerifyingDigit:
        return False

    # Calculating the second verifying digit
    digitsSum = sum(int(cpf[i]) * (11 - i) for i in range(10))
    remainder = digitsSum % 11

    if remainder < 2:
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = 11 - remainder

    # Checking the second verifying digit
    if int(cpf[10]) != secondVerifyingDigit:
        return False

    # Valid CPF
    return True

cpf = input("Type a valid CPF: ")
if (validate_cpf(cpf)):
    print(f"{cpf} is a valid CPF")
else:
    print(f"{cpf} is not a valid CPF")