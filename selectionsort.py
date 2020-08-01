# Selection Sort
"""Dividing the array into two sections sorted and unsorted list 
    Finding the minimum value in the whole list and placing it on the first index
    Now our first index is sorted and the rest value belongs to unsorted list
    Finding the minimum value from the unsorted list and placing it after the sorted list
    Follow same steps until all element belongs to sorted list"""


def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()


arr = [64, 25, 12, 22, 11]
selectionsort(arr)
print("Sorted List: ")
for i in range(len(arr)):
    print(arr[i], end=" ")
