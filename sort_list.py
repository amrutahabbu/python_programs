

def isSorted(list1):

    is_ascending = all(list1[i] <= list1[i + 1] for i in range(len(list1) - 1))
    is_descending = all(list1[i] >= list1[i + 1] for i in range(len(list1) - 1))

    return is_descending or is_ascending



inputList = [int(item) for item in input("Enter the list items : ").split()]
answerIsSorted= isSorted(inputList)
if(answerIsSorted):
    print("The list is sorted")
else:
    print("The  list is not sorted")
