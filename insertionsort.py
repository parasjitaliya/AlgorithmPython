"""
    do sorting with insertion sort for integer number and string
"""
import algoritham
import algoritham
n = int(input("enter the num of integers:"))
arr = []
for i in range(n):
    arr.append(int(input("enter the number or string for sort")))
insertion = algoritham.insertionSort(arr)