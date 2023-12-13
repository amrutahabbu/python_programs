import random

# Function to generate a random binary matrix
def generate_random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = [random.randint(0, 1) for _ in range(cols)]
        matrix.append(row)
    return matrix

def printMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")  # Use end=" " to print elements on the same line with space
        print()

# Function to find the row with the most 1s
def find_row_with_most_ones(matrix):
    max_ones_count = 0
    max_ones_row = None

    for i in range(len(matrix)):
        row = matrix[i]
        ones_count = row.count(1)
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            max_ones_row = i

    return max_ones_row, max_ones_count

# Function to find the column with the most 1s
def find_col_with_most_ones(matrix):
    max_ones_count = 0
    max_ones_col = None

    for j in range(len(matrix[0])):
        ones_count = sum(matrix[i][j] for i in range(len(matrix)))
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            max_ones_col = j

    return max_ones_col, max_ones_count


matrix = generate_random_matrix(4, 4)

# Print the matrix
print("Randomly generated matrix:")
printMatrix(matrix)

max_row, max_row_ones = find_row_with_most_ones(matrix)
max_col, max_col_ones = find_col_with_most_ones(matrix)

print(f"The largest row index {max_row} .")
print(f"The largest column index {max_col} .")
