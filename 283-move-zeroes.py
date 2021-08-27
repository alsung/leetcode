# Leetcode Question 283 [Easy]
# Move Zeroes

"""
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements. 

Note that you must do this in-place without making a copy of the array. 

Example 1: 
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2: 
Input: nums = [0]
Output: [0]

Constraints: 
    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^32 -1
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead. 
        """
        last_non_zero_index = 0

        if len(nums) <= 1:
            return nums
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1
            
        for i in range(last_non_zero_index, len(nums), 1):
            nums[i] = 0

        print(nums)

test = Solution()
nums_arr = [0,1,0,3,12]
test.moveZeroes(nums_arr)