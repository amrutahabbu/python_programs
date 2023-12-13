def binaryToDecimal(binaryString):

    if len(binaryString) == 0:
        return 0

    last_digit = int(binaryString[-1])

    # Recursively calculate the decimal value of the remaining binary digits
    remaining_binary = binaryString[:-1]
    decimal_value_of_remaining = binaryToDecimal(remaining_binary)

    decimal_value = (decimal_value_of_remaining << 1) | last_digit

    return decimal_value


binary_string = input("enter binary string 0'1s only")
decimal_value = binaryToDecimal(binary_string)
print(f"The decimal value of {binary_string} is {decimal_value}")
