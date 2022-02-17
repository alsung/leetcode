# Leetcode 191 [Easy]
# Number of 1 Bits

"""
Write a function that takes an unsigned integer and returns the number of '1' 
bits it has (also known as the Hamming weight).

Note:
 - Note that in some languages, such as Java, there is no unsigned integer 
    type. In this case, the input will be given as a signed integer type. It 
    should not affect your implementation, as the integer's internal binary 
    representation is the same, whether it is signed or unsigned.
 - In Java, the compiler represents the signed integers using 2's complement 
    notation. Therefore, in Example 3, the input represents the signed integer.
    -3.

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
"""


"""
Approach 1: 
If we take the binary integer and mod the number by 2, we will get 0 or 1
depending on if the last bit is 0 or 1, respectively. Then bitshifting 
the binary number by 1 and repeating until there are no values left and 
returning the sum of mod by 2 == 1. 
"""
# Time complexity: O(32) => O(1)
# Space complexity: O(1)
class Solution:
    def hammingWeight(self, n):
        res = 0
        while n > 0:
            res += n % 2
            n >> 1
        
        return res

# downside: have to look at every bit, even the 0s
# what if we have a number like 1000000000001 


"""
Approach 2: 
We can come up with a bit manipulation technique that allows us to run the loop
for as many number of 1 bits are in the number. Using n = n & (n - 1) basically
removes the last 1 bit from the binary number, and we can add 1 to our res count
for each loop. 
"""
# Time Complexity: O(32) => O(1). 
# Space complexity: O(1)
class Solution2:
    def hammingWeight(self, n):
        res = 0
        while n > 0:
            n &= (n-1)
            res += 1
        return res

