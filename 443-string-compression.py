# Leetcode Question 443 [Medium]
# String Compression

"""
Given an array of characters, chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating 
characters in chars:
    - if the group's length is 1, append the caracter to s. 
    - otherwise, append the character followed by the group's length. 

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer can be split into multiple characters in chars. 
After you are done modifying the input array, return the new length of the aray.
You must write an algorithm that uses only constant extra space. 
"""

class Solution:
    def compress(self, chars):
        res = []
        count = 1

        for i in range(1, len(chars)):
            if chars[i - 1] == chars[i]:
                count += 1
            else:
                res.append(chars[i - 1])
                if count > 1:
                    L = [i for i in str(count)]
                    res += L
                count = 1

        res.append(chars[-1])
        if count > 1:
            L = [i for i in str(count)]
            res += L
        count = 1
        chars[:] = res # copy res to chars array
        return len(chars)
