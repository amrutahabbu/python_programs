import math


def deviation(list1,meanvalue):

    numerator = 0
    for i in list1:
        numerator += ((i - meanvalue) ** 2)
        if(len(list1)>1):
            deviation_value = math.sqrt(numerator / (len(list1) - 1))
            return deviation_value
        else:
            return 0
def mean(list1):
    numerator = 0
    for i in list1:
        numerator += i
    mean = numerator / len(list1)

    return mean

inputList = [int(item) for item in input("Enter the list items : ").split()]
meanvalue = mean(inputList)

print("The meanv ois : " ,meanvalue)

deviation_value = deviation(inputList,meanvalue)

print("The deviation value is " ,deviation_value)
