# Leetcode Question 13

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

# Given a roman numeral, convert it to an integer. 

# Example: 
# input: s = "MCMXCIV"
# output: 1994

val_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        total = 0
        i = 0
        while i < len(s):
            # check if subtractive case
            if i+1 < len(s) and val_dict[s[i]] < val_dict[s[i+1]]:
                total += val_dict[s[i+1]] - val_dict[s[i]]
                i += 2
            
            # else, add value
            else: 
                total += val_dict[s[i]]
                i += 1
        
        return total
    
# Time Complexity: O(1)
# Space Complexity: O(1)
        