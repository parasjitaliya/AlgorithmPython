"""
 welcome to logic part of the algoritham
"""
class numberlogic:

    def __init__(self):
        self.list = []
    # -------------------------------logic for check two string is anagram or not-------------------------------

    def anagram_string(self, str1, str2):
        if sorted(str1) == sorted(str2):
            print("Strings are anagram")
        else:
            print("Strings are not anagram")

    # ------------------prime number range-----------------------------
    def prime_range(self, begin_range, end_range):
        prime_numbers_list = []
        for number in range(begin_range, end_range + 1):
            if number == 0 or number == 1:
                continue
            flag = 0
            for i in range(2, (number // 2) + 1):
                if number % i == 0:
                    flag = 1
                    break
            if (flag == 0):
                prime_numbers_list.append(number)
        return prime_numbers_list

    # ------------------------ pelindrom logic -------------------------
    def prime_palindrom(self, prime_number):
        palindroms_list = []
        for numbers in prime_number:
            temp = numbers
            sum = 0
            while numbers > 0:
                remainder = numbers % 10
                sum = sum * 10 + remainder
                numbers = numbers // 10
            if (temp == sum):
                palindroms_list.append(sum)
        return palindroms_list

    # -----------------------anagram number -------------------------

    def prime_anagram(self, prime_number):
        anagrams_list = []
        for start in range(len(prime_number) - 2):
            for start1 in range(start + 1, len(prime_number) - 1):
                num1 = str(prime_number[start])
                num2 = str(prime_number[start1])
                if sorted(num1) == sorted(num2):
                    anagrams_list.append(prime_number[start])
                    anagrams_list.append(prime_number[start1])
        return anagrams_list

class sorting:

    def __init__(self):
        self.list = []

    # ---------------------binary search ---------------------------

    def binarysearch(self, list, target):
        lower = 0
        upper = len(list) - 1
        while lower <= upper:
            mid = ((lower + upper) // 2)
            if list[mid] == target:
                globals()['pos'] = mid
                return True
            else:
                if list[mid] < target:
                    lower = mid + 1
                else:
                    upper = mid -1
        return False

    # ------------------- insertion sort ---------------------

    def insertionSort(self, arr):
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            tmp = arr[i]
            element = i - 1;
            while (element > 0 and arr[element] > tmp):
                arr[element + 1] = arr[element]
                element = element - 1
                arr[element + 1] = tmp
        print("Sorted array is:")
        for i in range(len(arr)):
            print(arr[i])

    # ----------------------bubble sort for integer ------------------------------

    def bubbleSort(self, arr):
        length = len(arr)
        # Traverse through all array elements
        for i in range(length - 1):
            # Last i elements are already in place
            for element in range(0, length - i - 1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[element] > arr[element + 1]:
                    temp = arr[element + 1]
                    arr[element + 1] = arr[element]
                    arr[element] = temp
        print("Sorted array is:")
        for i in range(len(arr)):
            print(arr[i])
    # -----------------------------mergesort -----------------------------------------------------------
    def mergeSort(self, list):
        if len(list) > 1:
            mid = len(list) // 2
            L = list[:mid]
            R = list[mid:]
            sorting.mergeSort(self, L)
            sorting.mergeSort(self, R)
            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    list[k] = L[i]
                    i += 1
                else:
                    list[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                list[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                list[k] = R[j]
                j += 1
                k += 1

    def printList(self, arr):
        for i in range(len(arr)):
            print(arr[i])

class generallogic:

    # ----------------------------------vending machine-----------------------------
    def vending_machine(self, avilable_notes, changing_amount):
        i = 0
        total_notes = 0
        while changing_amount > 0:
            # value divided by available notes
            notes = changing_amount // avilable_notes[i]
            if (notes > 0):
                # check for notes and print
                print(f"{notes} notes of {avilable_notes[i]} rupess")
                # count changing amount
                changing_amount = changing_amount % avilable_notes[i]
                total_notes += notes
            i += 1
        return total_notes

