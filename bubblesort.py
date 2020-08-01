# Bubble Sort
"""Comparing current element with adjacent element
    Repeatedly swapping the adjacent elements if they are in wrong order."""


def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()


arr = [5, 1, 4, 2, 8]
bubblesort(arr)
print("Sorted List: ")
for i in range(len(arr)):
    print(arr[i], end=" ")
