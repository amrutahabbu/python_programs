from Assignments.myLib import bubble_sort


def bubble_sort(l1):
    for j in range(0, len(l1)):
        for i in range(0, len(l1) - 1 - j):
            if l1[i] > l1[i + 1]:
                l1[i], l1[i + 1] = l1[i + 1], l1[i]

    return l1




inputList1 = [int(item) for item in input("Enter the list items : ").split()]
sortedArray1= bubble_sort(inputList1)


inputList2 = [int(item) for item in input("Enter the list items : ").split()]
sortedArray2= bubble_sort(inputList1)

merged_list = inputList1 + inputList2
finalSort = bubble_sort(merged_list)
print("The merged list is ",finalSort)