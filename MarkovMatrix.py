def isMarkovMatrix(matrix):

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        if num_rows != num_cols:
            return False


        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] < 0:
                    return False


        for i in range(num_rows):
            row_sum = sum(matrix[i])
            if not row_sum == 1.0:
                return False

        return True

inputrow1 = [eval(item) for item in input("Enter a row1 : ").split()]
inputrow2 = [eval(item) for item in input("Enter a row2 : ").split()]
inputrow3 = [eval(item) for item in input("Enter a row3 : ").split()]
matrix = [inputrow1,inputrow2,inputrow3]

result = isMarkovMatrix(matrix)
if result:
    print("It is a markovMatrix")
else:
    print("It is not a markovMatrix")