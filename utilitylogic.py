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
