


def bubble_sort(matrix):
    num_rows = len(matrix)

    for i in range(num_rows - 1):
        swapped = False
        for j in range(num_rows - i - 1):

            if matrix[j][1] > matrix[j + 1][1]:

                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
                swapped = True

        # If no swaps were made in this pass, the matrix is already sorted
        if not swapped:
            break
    return matrix



input_str = input("Enter student names and their scores separated by a space: ")
s1 = input_str.split()
input_str = input("Enter student names and their scores separated by a space: ")
s2 =input_str.split()
input_str = input("Enter student names and their scores separated by a space: ")
s3 = input_str.split()
input_str = input("Enter student names and their scores separated by a space: ")
s4 =input_str.split()
input_str = input("Enter student names and their scores separated by a space: ")
s5 = input_str.split()
input_str = input("Enter student names and their scores separated by a space: ")
s6 =input_str.split()
matrix = [s1,s2,s3,s4,s5,s6]

matrix1 = bubble_sort(matrix)

for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()