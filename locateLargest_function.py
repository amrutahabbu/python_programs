class Location:
    def __init__(self, row=0, column=0, maxValue=0.0):
        self.row = row
        self.column = column
        self.maxValue = maxValue

def locateLargest(matrix):

    #initialize

    maxValue= matrix[0][0]
    maxRow = 0
    maxColumn = 0

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):

            if matrix[i][j] > maxValue:
                maxValue = matrix[i][j]
                maxRow = i
                maxColumn= j


    location = Location(maxRow,maxColumn,maxValue)
    return location


inputrow1 = [int(item) for item in input("Enter a  row1 : ").split()]
inputrow2 = [int(item) for item in input("Enter a row2 : ").split()]
inputrow3 = [int(item) for item in input("Enter a row3 : ").split()]
matrix1= [inputrow1,inputrow2,inputrow3]
locationResult= locateLargest(matrix1)
print("Maximum Value is " ,locationResult.maxValue," at (",locationResult.row,",",locationResult.column,")")


