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

