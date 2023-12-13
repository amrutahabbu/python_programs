# Add matrices


def multiply_matrices(matrix1, matrix2):


    result = []
    sum=0
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            sum += matrix1[i][j] * matrix2[j][i]
            row.append(sum)
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


result = multiply_matrices(matrix1, matrix2)

for row in result:
    print(row)
