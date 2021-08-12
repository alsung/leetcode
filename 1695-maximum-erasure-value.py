# Leetcode Question 1695

# You are given an array of positive integers nums and want to erase a 
# subarray containing unique elements. The score you get by erasing the
# subarray is equal to the sum of its elements. 

# Return the maximum score you can get by erasing exactly one subarray

# An array b is called to be a subarray of a if it forms a contiguous 
# subsequence of a, that is, if it is equal to a[l], a[l+1],...,a[r] 
# for some (l,r).

# Example 1:
# input: nums = [4,2,4,5,6]
# output: 17
# explanation: optimal subarray is [2,4,5,6]

# input: nums = [5,2,1,2,5,2,1,2,5]
# output: 8
# explanation: [5,2,1] or [1,2,5]

# -----------------------------------------------------------------------------

# Brute Force Approach
# look for all possible subarrays that have unique elements and find their sum. 
# we can maintain the max sum found so far, if we find another, update max sum.

# 1. initialize start variable to index 0
# 2. for start goes from 0 to n
# 3. for end variable goes from start to n
# 4. maintain set and add every element to set
# 5. if end points to unique value, add value to current sum
# 6. else, stop
# 7. return max subarray sum

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        n = len(nums)
        curr_sc, max_sc = 0, 0
        seen = set() # use sets bc does not store duplicates
        while end < n:
            if nums[end] in seen:
                max_sc = max(max_sc, curr_sc)
                while nums[start] != nums[end]:
                    curr_sc -= nums[start]
                    seen.remove(nums[start])
                    start += 1
                curr_sc -= nums[start]
                seen.remove(nums[start])
                start += 1
                
            else:
                seen.add(nums[end])
                curr_sc += nums[end]
                end += 1
        
        return max(max_sc, curr_sc)
        

# 