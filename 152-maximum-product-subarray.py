# Leetcode Question 152 [Medium]
# Maximum Product Subarray

"""
Given an integer array nums, find a contiguous non-empty subarray within the 
array that has the largest product, and return the product. 

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
    1 <= nums.length <= 2 * 10^4
    -10 <= nums[i] <= 10
"""

"""
DP: compute max and max-abs-val (or min) for each prefix subarray
"""

"""
NeetCode Approach: https://www.youtube.com/watch?v=lXVy6YWFcRM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=7

Brute Force:
O(N^2) time, n * n = n^2

Patterns: 
We want to find the Max Product Subarray. We will also need to keep track of 
the minimum. 

Example:
all positive 
[1,2,3],4,5
1 * 2 * 3 * 4 * 5 = 
1   2   6  24  120
product always increasing if all positive

all negative
[-1,-2,-3] ,-4, -5
-1 * -2 * -3 * -4 * -5
-1    2   -6   24   -120
alternates signs if multiplied by negative

Edge Case:
when we encounter a '0', we need to reset our min and max to a neutral value, 1
If we reset min and max to 0, then we cannot keep recomputing min and max, will
retain value of 0 no matter what is multiplied. 
"""

class Solution:
    def maxProduct(self, nums):
        res = max(nums) # cannot set to 0 if array is [-1]
        curr_max = 1
        curr_min = 1

        for n in nums:
            if n == 0:
                curr_min = 1
                curr_max = 1
                continue # continue to next iteration of loop

            temp = curr_max * n # we want old curr_max when computing curr_min
            # if our curr_min is negative & n is negative
            curr_max = max(n * curr_max, n * curr_min, n) # if input is [-1, 8]
            curr_min = min(temp, n * curr_min, n) # example [-1, -8] = -8

            res = max(res, curr_max)

        return res

# Time Complexity: O(N)
# Space Complexity: O(1)

# =================================================================================

"""
1/20/2022

nums[]: int
find contiguous non-empty subarray within array with largest product, return product
"""

class Solution1:
    def maxProduct(self, nums):
        # Base case
        if len(nums) == 0:
            return 0
        
        # Set max and min so far
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        # iterate array 1 at a time from next number
        for i in range(1, len(nums)):
            curr = nums[i]
            calc_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            # update max_so_far
            max_so_far = calc_max

            # cache result
            result = max(result, max_so_far)
        
        # final result
        return result