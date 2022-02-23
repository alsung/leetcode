# LC 190 Easy
# Reverse Bits

"""
Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: n = 00000010100101000001111010011100
Output: 964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents 
the unsigned integer 43261596, so return 964176192 which its binary representation 
is 00111001011110000010100101000000.
"""

class Solution:
    # O(1) time | O(1) space
    def reverseBits(self, n):
        res = 0

        for i in range(32):
            bit = (n >> i) & 1 # to get the result bit in the 1s spot
            res = res | (bit << (31 - i)) # logic OR with largest bit to put bit in correct spot
        
        return res

sol = Solution()
print(sol.reverseBits(43261596)) # 964176192
print(sol.reverseBits(4294967293)) # 3221225471

# ================================================================================================
# Leetcode Approach:
"""
The key idea is that for a bit that is situated at index i, after the reversion, its position
should be 31 - i (note: index starts from 0).
 - we iterate through bit string of input integer, from right to left (i.e. n = n >> 1). To 
   retrieve the right-most bit of an integer, we apply the bit AND operation (i.e. n & 1)
 - for each bit, we reverse it to the correct position (i.e. (n & 1) << power). Then we 
   accumulate this reversed bit to the final result
 - when there are no more bits of '1' left (eg n == 0), we terminate the iteration
"""

class Solution2:
    # O(1) time | O(1) space
    def reverseBits(self, n):
        res = 0
        power = 31

        while n:
            res += (n & 1) << power # get first bit and add to res bit at correct reversed spot
            n = n >> 1 # shift input integer right by 1
            power -= 1 # move to next index of res bit string
        
        return res

sol2 = Solution2()
print(sol2.reverseBits(43261596)) # 964176192
print(sol2.reverseBits(4294967293)) # 3221225471