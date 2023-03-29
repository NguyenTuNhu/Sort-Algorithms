#examples sorting a list of number
#using sort functions

arr = [2,3,6,8,-6.5,-1]
print("Input: ", arr)

from bubble_sort import bubblesort
print("Sorting a list using Bubble sort algorithms: ", bubblesort(arr))

from insertion_sort import insertionsort
print("Sorting a list using Insertion sort algorithms: ", insertionsort(arr))

from selection_sort import selectionsort
print("Sorting a list using Insertion sort algorithms: ", selectionsort(arr))

