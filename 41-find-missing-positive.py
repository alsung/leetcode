# Leetcode Question 41 [Hard]

# Find Missing Positive

# Given an unsorted integer array nums, return the smallest missing positive number
# You must implement an algorithm that runs in O(n) time and uses constant space. 

# Example: 
# input: nums = [1,2,0]
# output: 3

# input: nums = [3,4,-1,1]
# output: 2

# input: nums = [7,8,9,11,12]
# output: 1

# Constraints:
# 1 <= nums.length <= 5 * 10^5
# -2^31 <= nums[i] <= 2^31 - 1

# Approach:
#   - let n = length of array
#   - ensure first missing positive is not 1, verify presence of 1
#   - first replace all zeros and negative numbers by 1s, we know that first missing
#     positive is smaller or equal to n + 1
#   - now have array of positive values from 1 to n 
#   - we want to use a hash map: positive number -> its presence for array
#   - dirty workaround: use str as a hash map by changing hash_str[i] to 1 when that
#     number i is found
#   - final idea: use index in nums as a hash key and sign of the element as a hash 
#     value which is presence detector
#   - negative sign of nums[2] means that number 2 is present in nums. positive sign
#     for nums[3] means that number 3 is not present (missing) in nums
#   - be careful with duplicates and ensure that the sign is only changed once

# Algorithm
#   - check if 1 is present in array. If not, you're done and return 1
#   - replace negative numbers, zeros, and numbers larger than n by 1s
#   - walk along array, change sign of a-th element if you meet number a. Be careful
#     with duplicates: change sign only once. Use index 0 to save any information
#     about presence of number n since index n is not available
#   - walk again along array. return index of first positive element
#   - if nums[0] > 0. return n. - number n in nums
#   - if on prev step you didnt find positive element in nums, return n + 1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        # Base case
        if 1 not in nums:
            return 1

        # Clean up negative, zeros, and nums > n by 1s
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # Use index as hash key and number sign as presence detector
        # for example, if nums[1] is negative, means that number '1'
        # is present in array
        # if nums[2] is positive - number 2 is missing
        for i in range(n):
            a = abs(nums[i])

            # if you meet number a in array - change sign of a-th element
            # be careful you only do this once
            if a == n:
                # meaning number n in the array, change nums[0] to negative
                # since we change value 0 to 1, we can use nums[0] as presence
                # detector for value n, more later 
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
        
        # Now index of first missing positive number is equal to first missing
        # positive
        for i in range(n):
            if nums[i] > 0:
                return i
        
        # if nums[0] is positive, value n is missing from nums
        if nums[0] > 0:
            return n

        # if no missing positive int, next missing positive is n + 1
        return n + 1

# Time Complexity: O(N)
# Space Complexity: O(1)