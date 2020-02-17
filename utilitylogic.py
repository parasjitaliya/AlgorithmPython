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
