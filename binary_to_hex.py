def binaryToHex(binaryValue):

        #decimalValue = int(binaryValue, 2)
        hexValue = hex(binaryValue)

        return hexValue


user_input_binary = eval(input("Enter a binary value: "))
hex_value = binaryToHex(user_input_binary)

print("Hexadecimal value:", hex_value)
