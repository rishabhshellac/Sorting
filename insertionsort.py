# Insertion Sort
"""Traversing the list from second index to last index
    Comparing the current element from the element residing behind it
    Swaping the values if current element is lesser than previous value one"""


def insertionsort(arr):
    for i in range(len(arr)):
        for j in range(0, i):
            if(arr[j] > arr[i]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()


arr = [12, 11, 13, 5, 6]
insertionsort(arr)
print("Sorted List: ")
for i in range(len(arr)):
    print(arr[i], end=" ")
