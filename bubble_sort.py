# Bubble sort

def bubble_sort(l1):
    for j in range(0, len(l1)):
        for i in range(0, len(l1) - 1 - j):
            if l1[i] > l1[i + 1]:
                l1[i], l1[i + 1] = l1[i + 1], l1[i]

    return l1

inputList = [int(item) for item in input("Enter the list items : ").split()]
sortedArray= bubble_sort(inputList)
print("The sorted List is ",sortedArray)

