# Leetcode Question 509 [Easy]
# Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
# Fibonacci sequence, such that each number is the sum of the two preceding 
# ones, starting from 0 and 1. That is, 

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1

# Given n, calculate F(n). 

# Example: 
# input: n = 2
# output: 1
# F(2) = F(1) + F(0) = 1 + 0 = 1

# input: n = 3
# output: 2
# F(3) = F(2) + F(1) = 1 + 1 = 2

# input: n = 4
# output: 3
# F(4) = F(3) + F(2) = 2 + 1 = 3

# Pseudocode:
# if n = 0, return 0
# if n = 1, return 1
# create array of size n + 1, so indices from 0..n
# initialize all values to 0
# initialize array[1] to 1
# fill out array by iterating from 2 to n + 1, where 
#   array[i] = array[i - 1] + array[i - 2]

class Solution(object):
    def fib(self, n): 
        if n <= 1:
            return n
        
        cache = [0] * (n + 1)
        cache[1] = 1

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]

# Time: O(n)
# Space: O(n)

# =============================================================================
# Iterative Bottom-Up Approach
#   - check if N <= 1, if it is, then return N
#   - we need 3 variables to store fib(N), fib(N - 1), and fib(N - 2)
#   - preset initial values:
#       - init current to 0
#       - init prev1 with 1, will represent fib(N - 1)
#       - init prev2 with 0, will represent fib(N - 2)
#   - iterate incrementally by 1, up to and including N, starting at 2, since 0
#     and 1 are pre-computed
#   - set current value to prev1 + prev2 because that is current computing val
#   - set prev2 value to prev1
#   - set prev1 value to current
#   - when we reach N+1, exit loop and return current value

class Solution2(object):
    def fib(self, n):
        if n <= 1:
            return n

        current = 0
        prev1 = 1
        prev2 = 0

        for i in range(2, n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return current

# Time: O(n)
# Space: O(1), no extra space needed



