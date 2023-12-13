def custom_find(substring, string):

    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return i
    return -1


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

index = custom_find(string1, string2)

if index != -1:
    print(f"'{string1}' is a substring of '{string2}' starting at index {index}.")
else:
    print(f"'{string1}' is not a substring of '{string2}'.")