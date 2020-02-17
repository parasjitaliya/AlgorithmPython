"""
  Take a range of 0 - 1000 Numbers and find the Prime numbers in that
--range. Store the prime numbers in a 2D Array, the first dimension
--represents the range 0-100, 100-200, and so on. While the second
--dimension represents the prime numbers in that range
"""
from utilitylogic import numberlogic
obj = numberlogic()

while True:
    try:
        begin_range=int(input("Enter the starting range :"))
        end_range=int(input("Enter the end of range :"))
        if begin_range>=0 and end_range>=0:
            break
        print("Invalid input! Enter positive range  ")
    except:
        print("Invalid input ")

prime = obj.prime_range(begin_range,end_range)
print(f"prime numbers in range of {begin_range}-{end_range} = \n {prime} ")