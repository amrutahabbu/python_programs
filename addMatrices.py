# Add matrices


def add_matrices(matrix1, matrix2):

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition")
        return []

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

print("Enter first matrix")
inputrow1 = [int(item) for item in input("Enter a  row1 : ").split()]
inputrow2 = [int(item) for item in input("Enter a row2 : ").split()]
inputrow3 = [int(item) for item in input("Enter a row3 : ").split()]
matrix1 = [inputrow1,inputrow2,inputrow3]
print("Enter second matrix")
inputrow1 = [int(item) for item in input("Enter a row1 : ").split()]
inputrow2 = [int(item) for item in input("Enter a  row2 : ").split()]
inputrow3 = [int(item) for item in input("Enter a  row3 : ").split()]
matrix2 = [inputrow1,inputrow2,inputrow3]


result = add_matrices(matrix1, matrix2)

for row in result:
    print(row)
