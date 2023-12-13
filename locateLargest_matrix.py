def locateLargest(matrix):
    if not matrix:
        return None  # Return None for an empty matrix

    max_element = matrix[0][0]  # Initialize with the first element
    max_row = 0
    max_col = 0

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for row in range(num_rows):
        for col in range(num_cols):
            element = matrix[row][col]
            if element > max_element:
                max_element = element
                max_row = row
                max_col = col

    return (max_row, max_col)

inputrow1 = [int(item) for item in input("Enter a  row1 : ").split()]
inputrow2 = [int(item) for item in input("Enter a row2 : ").split()]
inputrow3 = [int(item) for item in input("Enter a row3 : ").split()]
matrix = [inputrow1,inputrow2,inputrow3]

result = locateLargest(matrix)
print("The location of the largest element is at ", result)