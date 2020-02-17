import algoritham
"""
    do sorting with merge sort for integer number
"""
from utilitylogic import sorting
obj = sorting()
n = int(input("enter the num of integers:"))
arr = []
for i in range(n):
    arr.append((input("enter the number or string for sort")))

print("Given array is", end="\n")
obj.mergeSort(arr)
obj.printList(arr)
