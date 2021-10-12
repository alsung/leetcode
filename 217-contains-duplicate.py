# Leetcode Question 217 [Easy]
# Contains Duplicate

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 

Example 1: 
Input: nums = [1,2,3,1]
Output: true

Example 2: 
Input: nums = [1,2,3,4]
Output: false

Example 3: 
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = set()
        for i in range(len(nums)):
            if nums[i] in dup:
                return True
            else:
                dup.add(nums[i])
        return False

# Time: O(n)
# Space: O(n)

"""
1 line python solution
"""

class Solution1(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)

"""
Hashmap Approach
"""

class Solution2:
    def containsDuplicate(self, nums):
        map = {}

        for num in nums:
            if num in map:
                return True
            map[num] = 1
        return False

# Time Complexity: O(N), iterate only once over list
# Space Complexity: O(N), store a map of all non-duplicate values