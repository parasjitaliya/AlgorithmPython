"""
    do sorting with bubble sort for integer number and string
"""
from utilitylogic import sorting
obj=sorting()
n = int(input("enter the num of integers:"))
arr = []
for i in range(n):
    arr.append((input("enter the number or string for sort")))
obj.bubbleSort(arr)

