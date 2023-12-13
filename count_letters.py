def count_letters(input_string):
    count = 0

    for char in input_string:
          if char.isalpha():
            count += 1

    return count

user_input = input("Enter a string: ")
result = count_letters(user_input)
print("Number of letters:", result)