# Leetcode Question 268 [Easy]
# Missing Number

"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array. 

Follow up: Could you implement a solution using only O(1) extra space
complexity and O(n) runtime complexity? 

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range 
[0,3]. 2 is the missing number in the range since it does not appear in nums

Example 2: 
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range 
[0,2]. 2 is the missing number in the range since it does not appear in nums

Example 3: 
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range 
[0,9]. 8 is the missing number in the range since it does not appear in nums 

Example 4:
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range 
[0,1]. 1 is the missing number in the range since it does not appear in nums
"""

# Sorted Approach

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        
        nums.sort()

        # ensure n is at last index
        if nums[-1] != n:
            return n
        
        # ensure 0 is at first index
        if nums[0] != 0:
            return 0

        # if we get here, then missing number is in range [0, n]
        for i in range(1, n):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num

# Time Complexity: O(N log N)
# Space Complexity: O(1)

# Hash Set or Number Set Approach

class Solution1:
    def missingNumber(self, nums):
        n = len(nums) + 1
        num_set = set(nums)
        for num in range(n):
            if num not in num_set:
                return num