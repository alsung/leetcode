# Leetcode Question 238 [Medium]
# Product of Array Except Self

"""
Given an integer array, nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i]. 

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer. 

You must write an algorithm that runs in O(N) time without using the division 
property. 

Example 1: 
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2: 
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        prefix = 1
        postfix = 1

        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(n-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer

# Time Complexity: O(N). Two passes over the array, one in order and second in reverse. 
# Space Complexity: O(N). 