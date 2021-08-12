# Leetcode Question 1

# Given an array of integers nums and an integer target, return indices of the 
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice. You can return the answer in any order. 

# input: nums = [2,7,11,15] target = 9
# output: [0,1]
# output: Because nums[0] + nums[1] == 9, we return [0, 1]. 

# input: nums = [3,2,4] target = 6
# output: [1,2]

# input: nums = [3,3] target = 6
# output: [0,1]

# constraints: 
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# only one valid solution exists.

# Time: O(n)
# Space: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums): 
            x = target - num
            if x in nums_dict:
                return [nums_dict[x], i]
            else:
                nums_dict[num] = i

