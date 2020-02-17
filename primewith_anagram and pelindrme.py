import prime_range
from utilitylogic import numberlogic
obj = numberlogic()
prime_number=prime_range.prime

palindrom = obj.prime_palindrom(prime_number)
print(f"prime number is palindrom = {palindrom} ")
anagram = obj.prime_anagram(prime_number)
print(f"prime numbers is anagram = {anagram} ")