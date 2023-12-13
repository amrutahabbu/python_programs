


'''
input_list = []
input_list2=[]

while True:
    num = eval(input("Enter an integer (or any non-integer to finish): "))
    if(str(num).isdigit()):
     input_list.append(num)
    else:
     break

while len(input_list) > 0:
    length = len(input_list)
    for i in range(0,length):
        for j in range(1, 100 + 1):
            if input_list2.count([j]) != 0:
                print(i, "occurs", input_list2.count[j], "times")
            else:
                continue


'''


integer_counts = {}

def is_valid_number(num):
    return 1 <= num <= 100

while True:
    try:
        num = int(input("Enter an integer between 1 and 100 (or a non-integer to quit): "))
        if is_valid_number(num):
            if num in integer_counts:
                integer_counts[num] += 1
            else:
                integer_counts[num] = 1
        else:
            break  # Exit the loop if the input is not a valid integer
    except ValueError:
        break  # Exit the loop if the input is not a valid integer

print("\nInteger Counts:")
for number, count in sorted(integer_counts.items()):
    print(f"{number}: {count} times")
