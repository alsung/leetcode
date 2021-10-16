# Leetcode Question 33 [Medium]
# Search in Rotated Sorted Array

"""
There is an integer array nums sorted in ascending order (with distinct 
values). 

Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1],..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 
and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return 
the index of target if it is in nums, or -1 if it is not in nums. 

You must write an algorithm with O(log n) runtime complexity. 

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints: 
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique
nums is an ascending array that is possibly rotated
-10^4 <= target 10^4
"""

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            # check if mid in left sorted portion
            if nums[left] <= nums[mid]:
                # mid in left sorted portion

                if target > nums[mid] or target < nums[left]:
                    # search right
                    left = mid + 1
                else:
                    # target > mid and target > left, so search left
                    right = mid - 1
            
            else:
                # mid in right sorted portion
                if target < nums[mid] and target > nums[right]: # go left
                    right = mid - 1
                else:
                    # target > mid and < right, search right portion
                    left = mid + 1
        
        return -1

# Time Complexity: O(log N)
# Space Complexity: O(1)