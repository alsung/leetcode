# Leetcode Question 15
# 3Sum

# Given an integer array nums, return all triples [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets. 

# Example 1:
# input: nums = [-1,0,1,2,-1,-4]
# output: [[-1,-1,2],[-1,0,1]]

# input: nums = []
# output: []

# input: nums = [0]
# output: []

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        nums.sort()
        if nums == [] or nums == [0]:
            return []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                break;
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, sol)
        return sol
        
        
    def twoSumII(self, nums, i, sol):
        lo, hi = i+1, len(nums)-1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                sol.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

# Time Complexity: O(N^2) since twoSumII is O(N), and called N times
# Space Complexity: O(log N) to O(N), depending on implementation of sorting algo
    # for purpose of complexity analysis, ignore memory required for output

###############################################################################
# neetcode approach: https://www.youtube.com/watch?v=jzZsG8n2R9A&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=8

class Solution1: 
    def threeSum(self, nums):
        res = []

        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # meaning same value, don't use, skip value
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])

                    # [-2, -2, 0, 0, 2, 2]
                    #  L                R
                    # only have to update 1 pointer, our 2 conditions above will update the other pointer by itself
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # same value, keep shifting pointer
                        l += 1

        return res

# Time Complexity: O(N log N) + O(N^2), time to sort list + 2 nested loops
# Space Complexity: O(1) or O(N) depending on sort method used 