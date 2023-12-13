
def sumMajorDiagonal(m):


    diagonal_sum = 0
    for i in range(len(m)):
        if not len(m[i]) is len(m):
            print("Incoreeect input")
            return 0
        diagonal_sum += m[i][i]
    return diagonal_sum


inputrow1 = [int(item) for item in input("Enter a 4-4 row1 : ").split()]
inputrow2 = [int(item) for item in input("Enter a 4-4 row2 : ").split()]
inputrow3 = [int(item) for item in input("Enter a 4-4 row3 : ").split()]
inputrow4 = [int(item) for item in input("Enter a 4-4 row4 : ").split()]

inputMAtrix = [inputrow1,inputrow2,inputrow3,inputrow4]
answer = sumMajorDiagonal(inputMAtrix)
print("Sum of major diagnonal is : ",answer  )