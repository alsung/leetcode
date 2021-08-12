# Leetcode Question 12

# Roman numerals are represented by seven different symbols: I,V,X,L,C,D,M
# Symbol    Value
#   I         1
#   V         5
#   X         10
#   L         50
#   C         100
#   D         500
#   M         1000

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is IV, because the one is before the five so
# we subtract it making four. The same principle applies to the number nine, 
# which is IX.

# There are 6 instances:
# I can be placed before V and X to make 4 and 9
# X can be placed before L and C to make 40 and 90
# C can be placed before D and M to make 400 and 900

# Given an integer, convert it to a roman numeral. 

# Example: 
# input: num = 58
# output: "LVIII"

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                    (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                    (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        
        # loop through each digit
        for value, symbol in digits:
            # we dont want to continue looping if we're done
            if num == 0:
                break
            count, num = divmod(num, value)
            # append "count" copies of "symbol" to roman_digits
            roman_digits.append(symbol * count)
        
        return "".join(roman_digits)

# Time Complexity: O(1)
# Space Complexity: O(1)