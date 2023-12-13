input_list = []
while True:
    try:
        num = int(input("Enter an integer (or any non-integer to finish): "))
        input_list.append(num)
    except ValueError:
        break

print("Integers in reverse order:")
for num in reversed(input_list):
    print(num)

print("Without reversed function ")
#without reversed
len = len(input_list)
for i in range (len-1,-1,-1):
    print(input_list[i])

