# Leetcode Question 1911 [Medium]
# Maximum Alternating Subsequence Sum

# The alternating sum of a 0-indexed array is defined as the sum of the 
# elements at even indices minus the sum of the elements of odd indices. 

# For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4

# Given an array nums, return the maximum alternating sum of any subsequence 
# of nums (after reindexing the elements of the subsequence). 

# A subsequence of an array is a new array generated from the original array 
# by deleting some elements (possibly none) without changing the remaining 
# elements' relative order. For example, [2,7,4] is a subsequence of 
# [4,2,3,7,2,1,4], while [2,4,2] is not. 

# Example:
# input: nums = [4,2,5,3]
# output: 7
# optimal choice is sequence [4,2,5] with alternating sum (4 + 5) - 2 = 7

# input: nums = [5,6,7,8]
# output: 8
# it is optimal to choose the subsequence [8] with alternating sum 8

# input: nums = [6,2,1,2,4,5]
# output: 10
# it is optimal to choose the subsequence [6,1,5] with alternating sum 
# (6 + 5) - 1 = 10

# =============================================================================
# Recursive DFS Decision Tree Approach

class Solution1(object): 
    def maxAlternatingSum(self, nums):
        dp = {}

        # i = index, even = true/false
        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i, even) in dp:
                return dp[(i, even)]

            total = nums[i] if even else (-1 * nums[i])
            dp[(i, even)] = max(total + dfs(i + 1, not even), dfs(i + 1, even))
            return dp[(i, even)]
        return dfs(0, True)

# Time Complexity: O(n)
# Space Complexity: O(n)

# =============================================================================
# Dynamic Programming Approach

class Solution2(object):
    def maxAlternatingSum(self, nums):
        # sumEven, sum if first value added
        sumEven, sumOdd = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            tmpEven = max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)
            sumEven, sumOdd = tmpEven, tmpOdd

        return sumEven

# Time Complexity: O(n)
# Space Complexity: O(1), using two variables to store value instead of cache

